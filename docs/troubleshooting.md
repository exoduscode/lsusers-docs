# Troubleshooting

## `lsusers: command not found`

Confirm the package was installed through APT or Homebrew and inspect `PATH`:

```bash
command -v lsusers
lsusers --version
```

## `invalid choice: 'humans'`

Commands are singular:

```bash
lsusers human
```

## Conflicting output options

Choose only one of `--json`, `--csv`, or `--names`:

```bash
lsusers all --json
```

## An account has an unexpected type

On Linux, inspect its UID and allocation range:

```bash
getent passwd ACCOUNT_NAME
grep -E '^[[:space:]]*UID_(MIN|MAX)[[:space:]]' /etc/login.defs
```

On macOS, also verify that the username has no `_` prefix and the home is below
`/Users/`. See [Account classification](classification.md).

## Results differ from `/etc/passwd`

This is expected when NSS or directory services include LDAP, SSSD, or other
sources. Compare against `getent passwd` on Linux rather than assuming the file
is the complete system account database.

## Report a problem

Open normal bugs in the
[lsusers issue tracker](https://github.com/exoduscode/lsusers/issues). Report
security issues privately as described on the [Security](security.md) page.
