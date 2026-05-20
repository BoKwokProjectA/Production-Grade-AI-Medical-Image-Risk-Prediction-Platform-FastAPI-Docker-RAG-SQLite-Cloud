"""
Schemas used by the Copilot Studio support-agent endpoint.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class CopilotSupportRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=1000)
    conversation_id: Optional[str] = None
    user_role: Optional[str] = "user"


class CopilotSupportResponse(BaseModel):
    answer: str
    intent: str
    risk_level: str
    automation_allowed: bool
    escalation_required: bool
    sources: List[str]
    safety_note: str
