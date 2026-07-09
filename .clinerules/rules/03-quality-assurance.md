# Quality Assurance

## Documentation checklist

- [ ] Root README talk table matches `talks/` folders
- [ ] Python talks link to [python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice)
- [ ] No duplicated Python session markdown
- [ ] Assistant files describe speaker-series scope (not Applied Engineering)
- [ ] Mirror parity after governance edits (`sync-assistant-mirrors.ps1`)

## Python (Bedrock demos)

- [ ] Code under `talks/{id}/src/`
- [ ] Portable paths; no hardcoded machine paths
- [ ] `.env` not committed; `.env.example` documented

## Automation

- [ ] CI globs include `talks/` and `templates/`
- [ ] Skills parity between `.github/skills/` and `.cursor/skills/`

## Content review

- [ ] Talk links resolve
- [ ] Meetup URLs current for upcoming sessions