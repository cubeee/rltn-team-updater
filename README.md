# rltn-team-updater

Updates each team member's profile by visiting the pages

## Usage

Python:
```
TEAM_URL=/teams/XXXXXXXX ./updater.py
```

Docker:

```
$ docker build -t rltn-team-updater .
$ docker run --rm -it -e TEAM_URL=/teams/XXXXXXXX rltn-team-updater
```