# Trans for Doctors - Установка и использование

## Основные возможности

- 🎤 **STT (Speech-to-Text)** - транскрибация аудио с помощью Whisper
- 📚 **Knowledge Base** - база медицинских терминов
- 🤖 **LLM Коррекция** - исправление ошибок через OpenRouter API
  - Поддержка Google Gemini (рекомендуется)
  - Поддержка OpenAI GPT-4o
  - Поддержка Anthropic Claude
  - Множество других моделей через OpenRouter
- 📄 **Report Generation** - генерация DOCX отчетов

## CLI (uv) — end-to-end пайплайн

После `uv sync` доступен CLI-скрипт `transmed` для запуска ступенчатой архитектуры STT → KB → LLM → (отчет):

```bash
# Установка зависимостей
uv sync
uv pip install .[llm]  # для LLM-коррекции (OpenRouter)

# Запуск пайплайна
uv run transmed \
  --audio test_sound_ru.wav \
  --model . \
  --terms medical_terms.txt \
  --llm \
  --save-original --save-corrected --generate-report
```

Параметры:
- `--audio`: путь к .wav
- `--model`: папка с локальной Whisper-моделью (в корне проекта)
- `--terms`: файл терминов (Knowledge Base)
- `--llm` / `--no-llm`: включить/выключить коррекцию через LLM
- `--openrouter-key`: ключ OpenRouter (по умолчанию берет `OPENROUTER_API_KEY` из окружения)
- `--generate-report`: сформировать DOCX отчет
- `--results-dir`, `--logs-dir`: каталоги для выходных данных

💡 **OpenRouter:** Доступ к Google Gemini, GPT, Claude и другим моделям! См. [corrector/OPENROUTER.md](corrector/OPENROUTER.md)

## Быстрый старт (UV)

### Предварительные требования
- Python 3.13+ (torch GPU колеса требуют совместимую версию)
- Git
- Установленный менеджер uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy BypassUser -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Установка
```bash
git clone <ваш-репозиторий>
cd Trans_for_doctors

# uv сам создаст .venv и установит зависимости из pyproject.toml
uv sync
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### Подготовка CUDA (опционально)
uv sync ставит базовый torch. Для GPU поставьте колесо под свою версию CUDA 13.0:
```bash
# CUDA 13.0 (cu130)
uv pip install --upgrade \
  --index-url https://download.pytorch.org/whl/cu130 \
  torch torchvision torchaudio
```
Проверка GPU:
```bash
uv run python - <<'PY'
import torch
print(torch.cuda.is_available())
print(torch.cuda.device_name(0) if torch.cuda.is_available() else "cpu")
PY
```

### Запуск
```bash
uv run python run_demo.py \
  --device auto \
  --dtype float32 \
  --medical-prompt medical_terms.txt \
  --audio test_sound_ru.wav
```

- --device auto выберет CUDA если доступно, иначе CPU.
- Для GPU: --device cuda --dtype float32 
- Для CPU: --device cpu --dtype float32.

## Структура проекта
- run_demo.py — основной скрипт
- app/main.py — CLI для полного пайплайна (зарегистрирован как `transmed`)
- pyproject.toml — зависимости для uv
- requirements.txt — совместимость для pip
- Конфиги модели (config.json, generation_config.json, tokenizer_config.json и т.д.)
- medical_terms.txt — медицинская терминология
- Логи и результаты — папки logs/ и results/

## CLI параметры
- --audio — путь к аудиофайлу (по умолчанию test_sound_ru.wav)
- --medical-prompt — путь к файлу терминов
- --language — код языка (по умолчанию ru)
- --device — auto | cuda | cpu
- --dtype — auto | float32 | float16 | bfloat16

## Альтернатива: pip без uv
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run_demo.py
```

## Решение проблем
- Модель не скачивается: проверьте сеть и выполните huggingface-cli login.
- CUDA OOM: запустите на CPU (--device cpu) или используйте float16 на меньшей карте.
- Нет прав записи: убедитесь, что у вас есть права на каталог (chmod -R 755 ./).

## Windows .exe сборка (uv + PyInstaller)
Инструкции по сборке единичного `.exe` лежат в [packaging/windows/README.md](packaging/windows/README.md).
