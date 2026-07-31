# Command reference

## Synopsis

```text
lsusers [-h] [--json | --csv | --names] [--version]
        [{all,human,system,count}]
```

The positional command may appear before or after a format option.

## Commands

| Command | Behavior |
|---|---|
| `human` | List accounts classified as human. This is the default. |
| `system` | List root and accounts outside the platform's human-user policy. |
| `all` | List every record returned by the system account database. |
| `count` | Print human, system, and total counts. |

## Options

| Option | Behavior |
|---|---|
| `-h`, `--help` | Print help and exit. |
| `--version` | Print the installed version and exit. |
| `--json` | Emit an indented JSON array. |
| `--csv` | Emit CSV with a header row. |
| `--names` | Emit one username per line. |

The output options are mutually exclusive. They apply to `human`, `system`,
and `all`. `count` always uses its fixed text format.

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
