<section class="hero">
  <div class="eyebrow">Linux + macOS · open source</div>
  <h1>Know the users on your system.</h1>
  <p class="hero-copy"><code>lsusers</code> turns the system account database into clear, predictable output for people and scripts.</p>
  <div class="hero-actions">
    <a class="button primary" href="getting-started/">Install lsusers</a>
    <a class="button secondary" href="commands/">Command reference</a>
  </div>
</section>

<div class="terminal" role="figure" aria-label="Example output from the lsusers command">
  <div class="terminal-bar"><span></span><span></span><span></span><strong>Terminal</strong></div>
  <pre><code><span class="prompt">$</span> lsusers
USER   UID   TYPE   HOME         SHELL
-----  ----  -----  -----------  ---------
alice  1000  human  /home/alice  /bin/bash
dev    1001  human  /home/dev    /bin/zsh</code></pre>
</div>

<p class="example-note">The default command lists human accounts. Records vary with the host's account database.</p>

## One command, useful defaults

Run `lsusers` without arguments for a readable list of human accounts. No flags or configuration are required.

<div class="feature-grid">
  <div><span class="feature-number">01</span><strong>Easy to read</strong><p>Aligned output with the account name, UID, classification, home, and shell.</p></div>
  <div><span class="feature-number">02</span><strong>Automation-ready</strong><p>Stable JSON, CSV, and names-only formats for scripts and pipelines.</p></div>
  <div><span class="feature-number">03</span><strong>Platform-aware</strong><p>Explicit classification policies for Linux and macOS.</p></div>
  <div><span class="feature-number">04</span><strong>Secure delivery</strong><p>Signed APT metadata and an audited Homebrew installation flow.</p></div>
</div>

## Explore every account group

<div class="command-grid">
  <a href="commands/#lsusers-human"><code>lsusers human</code><span>Human accounts</span></a>
  <a href="commands/#lsusers-system"><code>lsusers system</code><span>System and service accounts</span></a>
  <a href="commands/#lsusers-all"><code>lsusers all</code><span>Every account record</span></a>
  <a href="commands/#lsusers-count"><code>lsusers count</code><span>Summary totals</span></a>
</div>

## Choose the right output

```bash
lsusers all --json    # APIs, jq, and structured automation
lsusers all --csv     # spreadsheets and tabular processing
lsusers all --names   # shell loops and quick inspection
```

[See practical pipelines and automation examples →](examples.md){ .next-link }

## Supported platforms

| Platform | Official installation | Account source |
|---|---|---|
| Ubuntu 24.04 | Signed ExodusCode APT repository | `pwd` / NSS |
| macOS | ExodusCode Homebrew tap | `pwd` / directory services |

Windows and other platforms fail explicitly instead of applying an incorrect classification policy.
