# Evaluation checklist

Use after dry runs and after live delivery.

## Demo reliability

- [ ] `bedrock_client.py` succeeds with current `.env` (default model matches `.env.example`)
- [ ] `agent.py` completes one full loop without unhandled exceptions
- [ ] Fallback narrative prepared if API is unavailable

## Content

- [ ] Agenda fits 60 minutes with 5-minute buffer
- [ ] Links in `links.md` are current
- [ ] Cost and data-handling called out in opening

## Attendee experience

- [ ] Clone → configure → run steps documented in talk README
- [x] At least one attendee question captured in talk README
