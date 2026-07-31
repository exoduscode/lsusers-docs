# Know the accounts on your system

`lsusers` is a small, script-friendly command for listing user accounts on
Linux and macOS. It classifies accounts as human or system users and emits
tables, JSON, CSV, or names-only output.

<div class="hero-actions">
  <a class="primary" href="getting-started/">Get started</a>
  <a href="examples/">Explore examples</a>
</div>

## Why lsusers?

<div class="feature-grid">
  <div><strong>Memorable</strong><br><code>lsusers human</code> is easy to discover and recall.</div>
  <div><strong>Portable</strong><br>Platform-specific policies support Linux and macOS.</div>
  <div><strong>Automation-ready</strong><br>Stable JSON, CSV, and names-only formats.</div>
  <div><strong>Secure distribution</strong><br>Signed APT metadata and audited Homebrew delivery.</div>
</div>

## A 30-second tour

```bash
# Human accounts in a readable table
lsusers human

# Every account as JSON
lsusers all --json

# System-account names, one per line
lsusers system --names

# Summary counts
lsusers count
```

```text
human: 2
system: 24
total: 26
```

## Supported platforms

| Platform | Official installation | Account source |
|---|---|---|
| Ubuntu 24.04 | Signed ExodusCode APT repository | `pwd` / NSS |
| macOS | ExodusCode Homebrew tap | `pwd` / directory services |

Windows and other platforms fail explicitly instead of applying an incorrect
classification policy.
