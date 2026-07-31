# Security policy

Security is an acceptance criterion for documentation, dependencies, build
automation, and deployment.

- Workflows use least privilege and immutable action SHAs.
- Python dependencies are locked with hashes.
- Dependency Review rejects moderate-or-higher known vulnerabilities.
- CodeQL analyzes repository automation.
- GitHub Pages deploys only from `main` through the protected
  `github-pages` environment.

Do not open a public issue for a suspected vulnerability. Use GitHub private
vulnerability reporting or follow the upstream
[lsusers security policy](https://github.com/exoduscode/lsusers/security/policy).
