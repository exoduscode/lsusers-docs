# Installation, updates, and removal

## Ubuntu 24.04

Follow the one-time repository setup in [Getting started](getting-started.md).
Normal updates then arrive through APT:

```bash
sudo apt update
sudo apt upgrade
```

Remove only the package:

```bash
sudo apt remove lsusers
```

To also remove the repository configuration:

```bash
sudo rm /etc/apt/sources.list.d/exoduscode.sources
sudo rm /usr/share/keyrings/exoduscode-archive-keyring.gpg
sudo apt update
```

## macOS

```bash
brew update
brew upgrade lsusers
```

Remove the package and, optionally, the tap:

```bash
brew uninstall lsusers
brew untap exoduscode/tap
```

## Verify installed artifacts

GitHub Release assets include `SHA256SUMS` and provenance attestations. A
downloaded artifact can be checked with:

```bash
sha256sum --check SHA256SUMS
gh attestation verify lsusers_<version>-1_all.deb \
  --repo exoduscode/lsusers
```
