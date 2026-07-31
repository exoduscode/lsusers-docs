# Output formats

All list formats use UID-then-username ordering.

## Table

```text
USER   UID   TYPE   HOME         SHELL
-----  ----  -----  -----------  ---------
alice  1000  human  /home/alice  /bin/bash
```

Use this format for people, not scripts.

## JSON

```json
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

JSON always returns an array. Empty results are `[]`.

## CSV

```csv
username,uid,gid,type,home,shell
alice,1000,1000,human,/home/alice,/bin/bash
```

CSV omits GECOS and uses `type` for the classification column.

## Names only

```text
alice
bob
```

One username is emitted per line. Empty results produce an empty payload.

## Count

`count` has a fixed text representation and does not become JSON or CSV when a
format flag is present.
