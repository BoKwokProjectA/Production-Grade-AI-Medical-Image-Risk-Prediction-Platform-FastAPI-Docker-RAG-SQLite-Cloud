"""
Routes used by Copilot Studio.
"""

from fastapi import APIRouter

from src.schemas.copilot_agent import CopilotSupportRequest, CopilotSupportResponse
from src.services.copilot_support_service import CopilotSupportService

copilot_router = APIRouter()


def get_support_service() -> CopilotSupportService:
    return CopilotSupportService()


@copilot_router.get("/agent/health")
async def copilot_agent_health():
    return {
        "status": "ok",
        "agent": "Skin Lesion Platform Support Agent",
        "scope": "technical_support_only",
    }


@copilot_router.post("/agent/support", response_model=CopilotSupportResponse)
async def ask_support_agent(request: CopilotSupportRequest):
    service = get_support_service()
    result = service.answer_question(request.question)
    return CopilotSupportResponse(**result)
