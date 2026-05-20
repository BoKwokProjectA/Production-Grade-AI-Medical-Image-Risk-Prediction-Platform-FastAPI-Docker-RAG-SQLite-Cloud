# Priority 5 evidence checklist

Use this checklist to capture proof that the real Copilot Studio agent was built and tested.

## Backend evidence

- `/api/v1/agent/health` returns 200
- `/api/v1/agent/support` returns a clean support answer
- Cloud Run service is live
- Swagger file validates successfully

## Power Platform evidence

- Custom connector imported
- Connector action exists: AskSkinLesionPlatformSupportAgent
- Connector test succeeds
- Connector response includes answer, intent, risk_level, sources, and safety_note

## Copilot Studio evidence

- Agent overview page
- SharePoint knowledge source connected
- Topics list
- Custom connector action added
- Test panel answering a technical question
- Test panel refusing a medical diagnosis question
- Publish page

## Minimum screenshots

Capture these for the portfolio:

1. Cloud Run endpoint working
2. Power Platform custom connector
3. Successful connector test
4. Copilot Studio agent overview
5. Knowledge source setup
6. Technical support answer
7. Medical safety refusal

## Portfolio note

This proves the agent is connected through the real stack:

- FastAPI backend
- Cloud Run deployment
- Power Platform custom connector
- Copilot Studio agent
- SharePoint knowledge source
- governance and safety docs
