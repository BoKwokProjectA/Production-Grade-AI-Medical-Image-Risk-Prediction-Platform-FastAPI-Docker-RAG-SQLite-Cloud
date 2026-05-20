# Topic: Upload Image

Trigger phrases:
- How do I upload an image?
- What file types are supported?
- My image upload failed.

Expected answer:
Explain that users upload an image through the prediction endpoint using multipart/form-data.
Mention supported image formats, file validation, and troubleshooting steps.

Action:
Use the support-agent API action when the user asks for project-specific upload behaviour.

Safety:
Do not interpret the uploaded image medically.
