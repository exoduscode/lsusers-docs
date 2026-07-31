# Commands and expected output

The simplest—and recommended—starting point is the command with no arguments:

```bash
lsusers
```

It lists human accounts in a readable table and behaves exactly like `lsusers human`.

!!! note "Example data"
    The names and totals below illustrate the output contract. Actual records depend on the host's NSS or directory-service configuration.

## Synopsis

```text
lsusers [-h] [--json | --csv | --names] [--version]
        [{all,human,system,count}]
```

The positional command may appear before or after a format option.

## `lsusers`

List human accounts using the default table format.

```console
$ lsusers
USER   UID   TYPE   HOME         SHELL
-----  ----  -----  -----------  ---------
alice  1000  human  /home/alice  /bin/bash
dev    1001  human  /home/dev    /bin/zsh
```

## `lsusers human`

Explicit form of the default command. It produces the same output as `lsusers`.

```console
$ lsusers human
USER   UID   TYPE   HOME         SHELL
-----  ----  -----  -----------  ---------
alice  1000  human  /home/alice  /bin/bash
dev    1001  human  /home/dev    /bin/zsh
```

## `lsusers system`

List root, service users, and other accounts outside the platform's human-user policy.

```console
$ lsusers system
USER    UID  TYPE    HOME       SHELL
------  ---  ------  ---------  -----------------
root    0    system  /root      /bin/bash
daemon  1    system  /usr/sbin  /usr/sbin/nologin
```

## `lsusers all`

List every record returned by the system account database.

```console
$ lsusers all
USER    UID   TYPE    HOME         SHELL
------  ----  ------  -----------  -----------------
root    0     system  /root        /bin/bash
daemon  1     system  /usr/sbin    /usr/sbin/nologin
alice   1000  human   /home/alice  /bin/bash
dev     1001  human   /home/dev    /bin/zsh
```

## `lsusers count`

Print fixed text totals for human, system, and all accounts.

```console
$ lsusers count
human: 2
system: 24
total: 26
```

## Output options

The output options apply to `lsusers`, `human`, `system`, and `all`. They are mutually exclusive. `count` always uses its fixed text format.

### `--names`

One username per line, suitable for shell pipelines:

```console
$ lsusers --names
alice
dev
```

### `--json`

An indented JSON array. Each record retains all account fields:

```console
$ lsusers human --json
[
  {
    "username": "alice",
    "uid": 1000,
    "gid": 1000,
    "gecos": "Alice Example",
    "home": "/home/alice",
    "shell": "/bin/bash",
    "user_type": "human"
  }
]
```

### `--csv`

CSV with a stable header row:

```console
$ lsusers human --csv
username,uid,gid,type,home,shell
alice,1000,1000,human,/home/alice,/bin/bash
```

## Utility options

| Option | Expected behavior |
|---|---|
| `-h`, `--help` | Print usage, commands, options, and exit. |
| `--version` | Print `lsusers 0.1.2` for the current release and exit. |

## Defaults and ordering

- Omitted command: `human`.
- Omitted format: aligned table.
- Ordering: UID ascending, then username ascending.

## Exit statuses

| Status | Meaning |
|---|---|
| `0` | Successful output, help, or version request. |
| `1` | Unsupported host platform. |
| `2` | Invalid arguments or conflicting output options. |

[Continue with real-world examples →](examples.md){ .next-link }
