# Practical examples

These examples favor structured formats when output will be consumed by
another command. Do not parse the human-readable table.

## Everyday inspection

List regular interactive accounts:

```bash
lsusers human
```

Review system and service accounts:

```bash
lsusers system
```

Print only names for a quick scan:

```bash
lsusers all --names
```

## Shell pipelines

Count account names without parsing the table:

```bash
lsusers human --names | sed '/^$/d' | wc -l
```

Check whether a specific account exists:

```bash
if lsusers all --names | grep -Fxq 'deploy'; then
  echo 'deploy account exists'
fi
```

Select accounts with Bash as their configured shell:

```bash
lsusers all --json | jq -r '.[] | select(.shell == "/bin/bash") | .username'
```

!!! warning
    Classification is descriptive, not authorization. Never grant privileges
    solely because an account is labeled `human`.

## JSON automation

Return usernames and numeric IDs:

```bash
lsusers human --json | jq '.[] | {username, uid}'
```

Find accounts with homes outside common user directories:

```bash
lsusers all --json | jq -r '
  .[]
  | select((.home | startswith("/home/")) | not)
  | [.username, .uid, .home]
  | @tsv
'
```

Create a username-to-UID object:

```bash
lsusers all --json | jq 'map({key: .username, value: .uid}) | from_entries'
```

## CSV workflows

Save a portable report:

```bash
lsusers all --csv >users.csv
```

Read it safely with Python's CSV parser:

```bash
python3 - <<'PY'
import csv

with open("users.csv", newline="", encoding="utf-8") as stream:
    for user in csv.DictReader(stream):
        if user["type"] == "human":
            print(user["username"], user["uid"])
PY
```

## Monitoring counts

```bash
lsusers count
```

```text
human: 2
system: 24
total: 26
```

For structured counting, calculate from JSON:

```bash
lsusers human --json | jq 'length'
```

## Compare two machines

Capture sorted names on each machine:

```bash
lsusers all --names | sort >host-a-users.txt
lsusers all --names | sort >host-b-users.txt
diff -u host-a-users.txt host-b-users.txt
```

NSS or directory-service configuration can legitimately make the results
different even when `/etc/passwd` is similar.
