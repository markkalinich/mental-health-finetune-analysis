# Documentation flags (verbosity and release hygiene)

<!-- doc-verbosity: public-ready -->

Use these markers so **humans and agents** can find docs that need trimming or review before a **public** push without relying on memory.

## Verbosity (machine-readable)

Put **this HTML comment on line 1** of the Markdown file (or immediately after the title `#` line if you prefer the title to stay first—then line 2 is fine). GitHub hides HTML comments in rendered view; they remain in source for search.

```html
<!-- doc-verbosity: public-ready -->
```

| Value | Meaning |
|-------|---------|
| `public-ready` | OK for a public audience; no planned trim. |
| `verbose-troubleshooting` | Detailed on purpose while debugging; **plan to shorten** before public release. |

**Find docs that still need trimming** (declared `verbose-troubleshooting`):

```bash
rg 'doc-verbosity: verbose-troubleshooting' --glob '*.md'
```

**List every file that declares a flag:**

```bash
rg 'doc-verbosity:' --glob '*.md'
```

## Optional human-visible line

Below the comment you may add a short visible line (optional, for readers who do not read raw source):

```markdown
> **Doc verbosity:** `verbose-troubleshooting` — trim before public (see `docs/DOCUMENTATION_FLAGS.md`).
```

Remove or rewrite that line when you promote the file to `public-ready`.

## Other flags

If we need more dimensions later (e.g. `<!-- doc-audience: internal -->`), add them in the same comment line or as separate `<!-- ... -->` lines and document them here.
