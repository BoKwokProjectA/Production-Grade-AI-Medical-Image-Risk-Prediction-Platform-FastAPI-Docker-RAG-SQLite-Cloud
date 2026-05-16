# Prediction Risk Review Workflow (Power Automate Demo)

This is a simple demonstration of how we would connect the FastAPI prediction endpoint to a Microsoft Power Automate workflow.

Purpose:
When the model returns a borderline prediction (probability between 0.48 and 0.52), automatically trigger a human review instead of giving an automatic answer.

How the flow works:
1. User uploads image to the /predict endpoint
2. FastAPI returns the probability
3. If probability is between 0.48 and 0.52 → trigger Power Automate
4. Power Automate creates a new item in a SharePoint list (or Dataverse)
5. Sends a notification to the reviewer via Teams or Outlook
6. Reviewer checks the image and adds feedback
7. Feedback is saved back to the prediction record

This shows human-in-the-loop safety and Microsoft 365 integration.

See workflow_details.md for the step-by-step flow.
