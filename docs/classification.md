# Account classification

`lsusers` selects a policy from the host platform. Labels describe common
platform conventions; they are not identity verification or authorization.

## Linux

Linux reads `UID_MIN` and `UID_MAX` from `/etc/login.defs`, using inclusive
defaults of 1000 and 60000 when valid values are unavailable.

```text
uid == 0                          -> system
UID_MIN <= uid <= UID_MAX
  and uid != 65534               -> human
otherwise                         -> system
```

UID 65534 (`nobody`) is always a system account.

## macOS

An account is human only when every condition is true:

```text
uid >= 500
username does not start with "_"
home starts with "/Users/"
```

## Directory services

The source is `pwd` and the operating system's account database. Linux NSS and
macOS directory services can include LDAP, SSSD, or network accounts. The tool
does not promise that every result originates in a local file.
