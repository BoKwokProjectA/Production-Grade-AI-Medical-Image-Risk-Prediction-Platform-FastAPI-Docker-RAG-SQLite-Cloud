# Skin Lesion Platform Support Agent

This folder contains the Copilot Studio setup files for the Skin Lesion Platform support agent.

The agent is for technical support only. It helps users understand:

- how the prediction endpoint works
- how to upload an image
- what the probability score means
- how to troubleshoot failed uploads
- how the model is governed
- what the medical safety limits are

The agent must not diagnose, classify, or interpret a user's skin lesion.

## Backend action

Copilot Studio calls the backend through a Power Platform custom connector.

Endpoint:

```text
POST /api/v1/agent/support
```

Example request:

```json
{
  "question": "How does the prediction endpoint work?",
  "conversation_id": "copilot-session-001",
  "user_role": "user"
}
```

Example response:

```json
{
  "answer": "...",
  "intent": "api_support",
  "risk_level": "Low",
  "automation_allowed": true,
  "escalation_required": false,
  "sources": ["src/api/routes.py"],
  "safety_note": "This is technical support only, not medical advice."
}
```

## Custom connector

Import this Swagger file into Power Platform:

```text
copilot_studio/openapi/isic_support_agent_connector.swagger.json
```

Before importing, replace this placeholder:

```text
REPLACE_WITH_CLOUD_RUN_HOST
```

Use the Cloud Run host only.

Example:

```text
my-api-service-1234567890.europe-west2.run.app
```

Do not include:

```text
https://
```

## Copilot Studio setup

Agent name:

```text
Skin Lesion Platform Support Agent
```

Agent purpose:

```text
Provide technical support for the Skin Lesion Platform. Do not provide medical diagnosis or treatment advice.
```

Core topics:

- Upload Image
- Prediction Endpoint
- Probability
- Failed Upload
- Governance
- Medical Safety

## Safety rule

If the user asks for diagnosis, treatment, or interpretation of a lesion, the agent must refuse and redirect the user to a qualified clinician.

The agent can still explain:

- how the platform works
- what the API returns
- what probability means technically
- why human review is used
- what the system limitations are
