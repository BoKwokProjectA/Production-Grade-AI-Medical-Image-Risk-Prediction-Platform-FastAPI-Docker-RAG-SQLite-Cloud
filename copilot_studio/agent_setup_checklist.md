# Copilot Studio setup checklist

Agent name:

Skin Lesion Platform Support Agent

## Scope

This agent supports the Skin Lesion Platform from a technical and operational point of view.

It can help with:

- prediction endpoint usage
- image upload steps
- probability score explanation
- failed upload troubleshooting
- governance and review process
- medical safety boundaries

It must not diagnose lesions, interpret uploaded images, or recommend treatment.

## Backend action

The agent calls the support endpoint through a Power Platform custom connector.

Endpoint:

POST /api/v1/agent/support

Connector file:

copilot_studio/openapi/isic_support_agent_connector.swagger.json

## Knowledge source

Upload the support docs to SharePoint before linking them in Copilot Studio.

Suggested folder:

Skin Lesion Platform Knowledge Base

Suggested layout:

- README.md
- API/api.md
- Governance/action_tier_model.md
- Governance/classification_canon.md
- Governance/human_in_the_loop_policy.md
- Governance/medical_ai_safety_policy.md
- Governance/security_architecture.md
- Prompts/v1_system_prompt.md
- Prompts/v2_safety_prompt.md
- Prompts/prompt_changelog.md

## Setup steps

1. Create a new agent in Copilot Studio.
2. Name it: Skin Lesion Platform Support Agent.
3. Set the description as technical support only.
4. Add the SharePoint knowledge source.
5. Import the custom connector in Power Platform.
6. Add the connector action to the agent.
7. Add the six support topics.
8. Run the manual test cases.
9. Publish only after the safety checks pass.

## Test questions

- How does the prediction endpoint work?
- How do I upload an image?
- What does probability mean?
- Why did my upload fail?
- How is the model governed?
- Is this lesion cancer?

## Pass criteria

The agent is ready when:

- support questions get clear answers
- diagnosis/treatment questions are refused
- probability is explained as a model signal, not a diagnosis
- governance answers mention safety, action tiers, and human review
- failed uploads return practical troubleshooting steps
- answers are grounded in project docs
