# Contributing to the documentation

Documentation changes are welcome through
[exoduscode/lsusers-docs](https://github.com/exoduscode/lsusers-docs).

## Requirements

1. Keep commands accurate for the current stable CLI.
2. Include practical examples when documenting behavior.
3. Never include real secrets or sensitive account data.
4. Preserve security warnings around account classification and shell usage.
5. Run the strict build and link checker.

```bash
mkdocs build --strict
python scripts/check_links.py site
```

Behavioral documentation should reference the corresponding implementation or
test in [exoduscode/lsusers](https://github.com/exoduscode/lsusers).
