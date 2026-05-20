# Human-in-the-Loop Policy

When the agent detects high uncertainty or risk:
1. Prediction probability between 0.45 and 0.55 → flag for review
2. Any medical-related query → automatic refusal + escalation option
3. User feedback marked as negative → logged for review

Escalation creates a record in the prediction database and can trigger a simple notification workflow (future Power Automate integration).


