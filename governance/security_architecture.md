# Security Architecture

- All predictions and RAG queries run through the FastAPI backend
- No user data or uploaded images are stored permanently
- Input validation on image uploads (size, type)
- Structured error handling with no stack trace leakage
- Prompts and system instructions are version controlled
- Governance rules are enforced at prompt level and evaluation level
- Human review triggered for any high-risk action

This setup follows basic secure AI deployment practices.
