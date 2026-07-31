# Security

## Safe interpretation

`human` and `system` are convenience classifications. They must not be used as
the sole input for access control, privilege assignment, account deletion, or
incident-response decisions.

Treat account names, GECOS values, homes, and shells as untrusted system data
when forwarding output to terminals, logs, templates, or other commands.

## Distribution trust

Ubuntu packages are delivered through a signed repository using a dedicated
archive key. Homebrew uses a formula with an immutable source checksum.
GitHub Release artifacts are tested before publication and include checksums
and signed provenance.

APT signing-key fingerprint:

```text
C85D DAF2 A38C A242 A745 D9DE 5A40 25DA 3610 A2EC
```

## Report vulnerabilities privately

Do not publish suspected vulnerabilities or sensitive account data in an
issue. Use
[GitHub private vulnerability reporting](https://github.com/exoduscode/lsusers/security/advisories/new)
or follow the
[upstream security policy](https://github.com/exoduscode/lsusers/security/policy).
