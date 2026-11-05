#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTTP client for an OpenAI-compatible vLLM server.

Every runner builds its request through this class. A checkpoint that ships a
chat template is a /chat/completions request. A checkpoint whose own files
have no chat template is one string, the message texts in order separated by
a blank line, posted to /completions. That is the pretrained release that
did not ship a role wrapper.

config/serving_repairs.csv is applied here and by the serving script:

  fold_system      1 -> a leading system message is prepended to the first user
                        message (Gemma 2 templates raise on a system role).
  tokenizer_from   the serving script points vLLM at that repo's tokenizer.
                   The request stays a chat, because those rows exist to supply
                   a chat template the served repo did not include.
"""
import csv
import json
import requests
import aiohttp
import asyncio
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from config import EvaluationConfig

REPAIRS_CSV = Path(__file__).resolve().parent.parent / "config" / "serving_repairs.csv"
HF_MODELS = Path("/home/mkalinich/hf_models")


def tokenizer_has_chat_template(directory: Path) -> bool:
    """True when this directory ships a non-empty chat template."""
    jinja = directory / "chat_template.jinja"
    if jinja.is_file() and jinja.read_text(encoding="utf-8").strip():
        return True
    config_path = directory / "tokenizer_config.json"
    if not config_path.is_file():
        return False
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    template = config.get("chat_template")
    return isinstance(template, str) and bool(template.strip())


def prompts_as_one_string(model_id: str, repair: Dict[str, str]) -> bool:
    """True when the served checkpoint has no chat template of its own.

    tokenizer_from means the server is given another repo's tokenizer so that
    an instruction model can keep its chat format. A model id with no local
    tokenizer file stays a chat request: this client does not invent a format
    for a checkpoint it cannot see.
    """
    if (repair.get("tokenizer_from") or "").strip():
        return False
    directory = HF_MODELS / model_id.replace("/", "__")
    if not (directory / "tokenizer_config.json").is_file() and not (directory / "chat_template.jinja").is_file():
        return False
    return not tokenizer_has_chat_template(directory)


def load_serving_repairs(path: Path = REPAIRS_CSV) -> Dict[str, Dict[str, str]]:
    """hf_id -> row of config/serving_repairs.csv. Missing file -> no repairs."""
    if not path.is_file():
        return {}
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["hf_id"]: row for row in csv.DictReader(handle)}


class ChatAPIError(Exception):
    """A chat-completions request failed (HTTP error, timeout, or bad JSON)."""
    pass



class ChatCompletionsClient:
    """POSTs to {base_url}/chat/completions. No server-specific SDK."""
    
    def __init__(self, config: EvaluationConfig):
        """
        Initialize the API client.
        
        Args:
            config: Configuration object with API settings
        """
        self.config = config
        self.base_url = config.base_url.rstrip('/')
        self.repair: Dict[str, str] = load_serving_repairs().get(config.model, {})
        self.fold_system: bool = self.repair.get("fold_system", "0") == "1"
        self.one_string: bool = prompts_as_one_string(config.model, self.repair)

    def _messages(self, messages: list) -> List[Dict[str, str]]:
        """Validated copy of ``messages`` with this model's fold applied.

        With fold_system, a leading system message is removed and its text is
        prepended to the first user message, separated by a blank line. Nothing
        else is merged or reordered.
        """
        copied = self.copy_chat_messages(messages)
        if self.fold_system and copied[0]["role"] == "system":
            if len(copied) < 2 or copied[1]["role"] != "user":
                raise ChatAPIError("fold_system needs a user message right after the system message")
            system_text = copied.pop(0)["content"]
            copied[0] = {"role": "user", "content": f"{system_text}\n\n{copied[0]['content']}"}
        return copied

    def _prompt_text(self, messages: list) -> str:
        """The task words in order. No role labels are added."""
        copied = self.copy_chat_messages(messages)
        return "\n\n".join(message["content"] for message in copied)

    def _request(
        self,
        messages: list,
        *,
        max_tokens: int,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
    ) -> Tuple[str, Dict[str, Any]]:
        """Path and body for one generation.

        Sampling fields are included only when the caller passes them.
        A chat template's extra kwargs are included only on a chat request.
        """
        if self.one_string:
            payload: Dict[str, Any] = {
                "model": self.config.model,
                "prompt": self._prompt_text(messages),
                "max_tokens": max_tokens,
                "stream": False,
            }
        else:
            payload = {
                "model": self.config.model,
                "messages": self._messages(messages),
                "max_tokens": max_tokens,
                "stream": False,
            }
            template_kwargs = getattr(self.config, "chat_template_kwargs", None)
            if template_kwargs:
                payload["chat_template_kwargs"] = template_kwargs
        if temperature is not None:
            payload["temperature"] = temperature
        if top_p is not None:
            payload["top_p"] = top_p
        path = "completions" if self.one_string else "chat/completions"
        return path, payload

    @staticmethod
    def _check_http_error(status: int, error_text: str, *, include_body: bool = True) -> None:
        if "System role not supported" in error_text:
            raise ChatAPIError(
                f"API request failed with status {status}: the model's chat template rejects a "
                f"system role; add a fold_system=1 row for it in {REPAIRS_CSV}"
            )
        detail = f": {error_text}" if include_body else ""
        raise ChatAPIError(f"API request failed with status {status}{detail}")
        
    def call_chat_completion(self, system_prompt: str, text: str) -> Dict[str, Any]:
        """
        One chat completion from a system prompt and a user text.
        
        Args:
            system_prompt: System prompt to guide model behavior
            text: User text to process
            
        Returns:
            Full API response as dictionary
            
        Raises:
            ChatAPIError: If API request fails
        """
        path, payload = self._request(
            [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            top_p=self.config.top_p,
        )
        url = f"{self.base_url}/{path}"

        try:
            response = requests.post(
                url, 
                json=payload, 
                timeout=self.config.request_timeout
            )
            if response.status_code != 200:
                self._check_http_error(response.status_code, response.text)
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise ChatAPIError(f"API request failed: {e}") from e
        except ValueError as e:
            raise ChatAPIError(f"Invalid JSON response: {e}") from e
    
    async def call_chat_completion_async(self, system_prompt: str, text: str) -> Dict[str, Any]:
        """
        Async form of call_chat_completion.
        
        Args:
            system_prompt: System prompt to guide model behavior
            text: User text to process
            
        Returns:
            Full API response as dictionary
            
        Raises:
            ChatAPIError: If API request fails
        """
        path, payload = self._request(
            [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            top_p=self.config.top_p,
        )
        url = f"{self.base_url}/{path}"

        try:
            timeout = aiohttp.ClientTimeout(total=self.config.request_timeout)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(url, json=payload) as response:
                    if response.status != 200:
                        self._check_http_error(response.status, await response.text())
                    return await response.json()
                    
        except aiohttp.ClientError as e:
            raise ChatAPIError(f"API request failed: {e}") from e
        except asyncio.TimeoutError as e:
            raise ChatAPIError(f"Request timeout: {e}") from e
        except ValueError as e:
            raise ChatAPIError(f"Invalid JSON response: {e}") from e

    @staticmethod
    def copy_chat_messages(messages: list) -> List[Dict[str, str]]:
        """Copy a chat message list without merging turns.

        Each element is one message with role and content. Roles stay
        system, user, or assistant. This does not build a system-plus-user pair.
        """
        if not isinstance(messages, list) or not messages:
            raise ChatAPIError("messages must be a non-empty list")
        copied: List[Dict[str, str]] = []
        allowed = {"system", "user", "assistant"}
        for index, message in enumerate(messages):
            if not isinstance(message, dict):
                raise ChatAPIError(f"message {index} must be an object")
            role = message.get("role")
            content = message.get("content")
            if role not in allowed:
                raise ChatAPIError(f"message {index} has an unsupported role")
            if not isinstance(content, str):
                raise ChatAPIError(f"message {index} content must be a string")
            copied.append({"role": role, "content": content})
        return copied

    def build_messages_completion_payload(
        self,
        messages: list,
        *,
        max_tokens: int,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Body for one completion over an existing message list.

        Temperature and top_p are sent only when the caller passes them.
        A call that leaves them out keeps the server default. The
        EvaluationConfig fields of the same name are not read here.
        chat_template_kwargs is included only when the config has that
        attribute set. The model's fold_system repair, if any, applies.
        """
        if isinstance(max_tokens, bool) or not isinstance(max_tokens, int) or max_tokens < 1:
            raise ChatAPIError("max_tokens must be a positive int")
        _path, payload = self._request(
            messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )
        return payload

    async def call_chat_completion_messages_async(
        self,
        messages: list,
        *,
        max_tokens: int,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
    ) -> Dict[str, Any]:
        """POST the generation for this checkpoint.

        A checkpoint with a chat template is /chat/completions. A checkpoint
        with none is one string on /completions. Temperature and top_p are
        sent only when the caller passes them. chat_template_kwargs is sent
        only on a chat request, and only when the config has that attribute set.
        """
        payload = self.build_messages_completion_payload(
            messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )
        url = f"{self.base_url}/{'completions' if self.one_string else 'chat/completions'}"
        try:
            timeout = aiohttp.ClientTimeout(total=self.config.request_timeout)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(url, json=payload) as response:
                    if response.status != 200:
                        # Body is read only for the template check, not kept: MHB error
                        # bodies can echo item text and the canary marker.
                        self._check_http_error(response.status, await response.text(), include_body=False)
                    return await response.json()
        except aiohttp.ClientError as e:
            raise ChatAPIError(f"API request failed: {e}") from e
        except asyncio.TimeoutError as e:
            raise ChatAPIError(f"Request timeout: {e}") from e
        except ValueError as e:
            raise ChatAPIError(f"Invalid JSON response: {e}") from e

    def extract_content(self, response: Dict[str, Any]) -> str:
        """
        Extract message content from API response.
        
        Args:
            response: Full API response dictionary
            
        Returns:
            Message content string, or empty string if not found
        """
        try:
            choice = response.get("choices", [{}])[0]
        except (IndexError, TypeError):
            return ""
        message = choice.get("message") if isinstance(choice, dict) else None
        if isinstance(message, dict):
            return message.get("content") or ""
        if isinstance(choice, dict):
            return choice.get("text") or ""
        return ""
    
    def warmup_model(self, max_retries: int = 3, retry_delay: float = 2.0) -> bool:
        """
        Ensure model is loaded by sending a simple warmup request.
        
        This sends a minimal request to force LM Studio to load the model
        before we start the main batch of requests.
        
        Args:
            max_retries: Maximum number of warmup attempts
            retry_delay: Delay between retries in seconds
            
        Returns:
            True if model is confirmed loaded, False otherwise
        """
        warmup_prompt = "Respond with only the word 'ready'."
        warmup_text = "Are you ready?"
        
        for attempt in range(max_retries):
            try:
                print(f"  🔄 Warming up model {self.config.model}... (attempt {attempt + 1}/{max_retries})")
                start_time = time.time()
                
                response = self.call_chat_completion(warmup_prompt, warmup_text)
                
                elapsed = time.time() - start_time
                content = self.extract_content(response)
                
                if response and "choices" in response:
                    print(f"  ✅ Model loaded and responding ({elapsed:.1f}s)")
                    return True
                    
            except ChatAPIError as e:
                error_msg = str(e)
                if "Model does not exist" in error_msg or "Failed to load model" in error_msg:
                    print(f"  ⏳ Model not loaded yet, waiting {retry_delay}s...")
                    time.sleep(retry_delay)
                else:
                    print(f"  ⚠️ Warmup error: {error_msg[:100]}")
                    time.sleep(retry_delay)
        
        print(f"  ❌ Failed to warm up model after {max_retries} attempts")
        return False
    
