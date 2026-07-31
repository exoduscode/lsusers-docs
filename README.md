# lsusers documentation

Source for the official `lsusers` documentation website:

<https://exoduscode.github.io/lsusers-docs/>

The site is built with MkDocs and deployed through GitHub Pages. Documentation
changes require a successful strict build, internal-link validation, dependency
review, and CodeQL analysis.

## Local preview

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --require-hashes -r requirements.lock
mkdocs serve
```

## Validate

```bash
mkdocs build --strict
python scripts/check_links.py site
```
