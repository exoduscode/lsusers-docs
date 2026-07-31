# Getting started

## Install

### Ubuntu 24.04

Configure the signed repository once:

```bash
curl -fsSL https://exoduscode.github.io/apt/keys/exoduscode-archive-keyring.gpg \
  | sudo tee /usr/share/keyrings/exoduscode-archive-keyring.gpg >/dev/null

sudo tee /etc/apt/sources.list.d/exoduscode.sources >/dev/null <<'EOF'
Types: deb
URIs: https://exoduscode.github.io/apt
Suites: noble
Components: main
Signed-By: /usr/share/keyrings/exoduscode-archive-keyring.gpg
EOF

sudo apt update
sudo apt install lsusers
```

### macOS

```bash
brew install exoduscode/tap/lsusers
```

## Verify

```bash
lsusers --version
lsusers count
```

## First commands

With no positional command, `lsusers` defaults to `human`:

```bash
lsusers
lsusers human
```

Use `system` for service and operating-system accounts, or `all` for every
record returned by the system account database:

```bash
lsusers system
lsusers all
```

Continue with the [command reference](commands.md) or jump directly to the
[practical examples](examples.md).
