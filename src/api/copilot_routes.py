"""
Copilot Studio connector routes.


"""

from fastapi import APIRouter

from src.schemas.copilot_agent import (
    CopilotSupportRequest,
    CopilotSupportResponse,
)
from src.services.copilot_support_service import CopilotSupportService


copilot_router = APIRouter()


@copilot_router.get("/agent/health")
async def copilot_agent_health():
    """
    Health check endpoint for the Copilot Studio custom connector.
    """
    return {
        "status": "ok",
        "agent": "Skin Lesion Platform Support Agent",
        "scope": "technical_support_only",
    }


@copilot_router.post(
    "/agent/support",
    response_model=CopilotSupportResponse,
)
async def ask_copilot_support_agent(request: CopilotSupportRequest):
    """
    Main support endpoint called by Copilot Studio.
    """
    service = CopilotSupportService()

    result = service.answer_question(
        question=request.question,
        conversation_id=request.conversation_id,
        user_role=request.user_role,
    )

    return CopilotSupportResponse(**result)
