# Action Tier Model

This table defines what the Skin Lesion Platform Support Agent is allowed to do.

| Action                              | Risk Level | Automation Allowed? | Notes |
|-------------------------------------|------------|---------------------|-------|
| Explain how the prediction endpoint works | Low       | Yes                 | Technical only |
| Explain probability score and model architecture | Low       | Yes                 | Factual only |
| Help with image upload or troubleshooting | Low       | Yes                 | Standard support |
| Answer general project or API questions | Low       | Yes                 | Grounded in documentation |
| Interpret any uploaded image medically | High      | No                  | Always refuse |
| Give diagnosis, treatment or medical advice | Prohibited | No               | Immediate refusal + doctor recommendation |
| Flag uncertain prediction for human review | Medium    | Yes (with review)   | Creates SharePoint item |

Reviewed: 2026-05-15
