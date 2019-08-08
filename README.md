# Facebook Brute Forcer Tool

Brute force tool for tests accounts with facebook

## How to set up?

Use docker for your local environment.

```
./fb-bruteforcer --build
```

## How to execute the tool?

Follow this steps:

1. Add all your users in `data/users.txt` file.
2. Add all password combinations in `data/passwords.txt` file.

```
./fb-bruteforcer --exec
```

**One report will be created on `data/report`***
