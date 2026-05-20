"""
Support service for the Copilot Studio agent.

Keep this service lightweight. Cloud Run should not load embeddings or build
a vector index during API startup.
"""

from typing import Dict, List


class CopilotSupportService:
    def __init__(self):
        self.medical_terms = [
            "diagnose",
            "diagnosis",
            "cancer",
            "melanoma",
            "benign",
            "malignant",
            "treatment",
            "treat",
            "medicine",
            "should i see",
            "what is this lesion",
            "is this lesion",
            "is this mole",
            "is this dangerous",
            "do i have",
            "am i sick",
            "what should i do medically",
        ]

    def answer_question(self, question: str) -> Dict:
        clean_question = question.strip()
        intent = self._classify_intent(clean_question)

        if intent == "medical_advice":
            return self._medical_refusal()

        return {
            "answer": self._build_answer(intent),
            "intent": intent,
            "risk_level": self._risk_level_for_intent(intent),
            "automation_allowed": True,
            "escalation_required": False,
            "sources": self._sources_for_intent(intent),
            "safety_note": (
                "This agent provides technical support for the platform. "
                "It does not provide medical diagnosis, treatment advice, "
                "or clinical interpretation of uploaded images."
            ),
        }

    def _classify_intent(self, question: str) -> str:
        q = question.lower()

        if any(term in q for term in self.medical_terms):
            return "medical_advice"

        if any(term in q for term in ["failed", "fail", "error", "troubleshoot", "400", "500"]):
            return "failed_upload_support"

        if any(term in q for term in ["upload", "image file", "file type", "multipart"]):
            return "image_upload_support"

        if any(term in q for term in ["endpoint", "api", "predict", "/predict", "request", "response"]):
            return "api_support"

        if any(term in q for term in ["probability", "score", "confidence", "risk score"]):
            return "prediction_explanation"

        if any(term in q for term in ["govern", "governance", "safety", "limitation", "human review", "audit"]):
            return "governance"

        return "general_platform_support"

    def _build_answer(self, intent: str) -> str:
        answers = {
            "api_support": (
                "The prediction endpoint accepts an uploaded image, validates the file, "
                "passes it through the inference pipeline, and returns a structured prediction response.\n\n"
                "A typical response includes the uploaded image identifier, the model probability, "
                "the prediction label, and model/version metadata used for traceability.\n\n"
                "The endpoint is intended for platform workflow support and risk review. "
                "Its output should not be treated as a medical diagnosis."
            ),
            "image_upload_support": (
                "To upload an image, the client should send the file to the prediction endpoint "
                "as a multipart/form-data request.\n\n"
                "The platform checks that the uploaded file is an image before sending it to the "
                "prediction service. If the file is not recognised as an image, the API should reject "
                "the request instead of passing it into the model.\n\n"
                "For Copilot Studio users, this should be explained as a technical upload process, "
                "not as a clinical image review."
            ),
            "failed_upload_support": (
                "A failed upload is usually caused by one of these issues:\n\n"
                "- the file was not sent as multipart/form-data\n"
                "- the uploaded file is not a supported image type\n"
                "- the request used the wrong endpoint URL\n"
                "- the file field name does not match the API contract\n"
                "- the backend service is unavailable or returned an internal error\n\n"
                "Check the request format first, then confirm the endpoint health, and finally "
                "review the API logs for the exact failure reason."
            ),
            "prediction_explanation": (
                "The probability value is the model's numerical output for the prediction request. "
                "It should be read as a model-generated risk signal, not as a diagnosis.\n\n"
                "A higher probability can be used by the platform to trigger review workflows, "
                "such as human-in-the-loop review, but it should not be used to tell a user that "
                "they do or do not have a medical condition.\n\n"
                "The correct framing is: probability supports workflow prioritisation and review, "
                "not clinical decision-making."
            ),
            "governance": (
                "The model is governed through safety rules, action tiers, human review, and clear "
                "limits on what the system is allowed to automate.\n\n"
                "Low-risk actions, such as explaining API usage or upload steps, can be automated. "
                "Medium-risk actions, such as flagging uncertain predictions, should route to human "
                "review. High-risk or prohibited actions, such as diagnosing a lesion or recommending "
                "treatment, must not be automated.\n\n"
                "The agent should always make the medical safety boundary clear."
            ),
            "general_platform_support": (
                "I can help with technical questions about the Skin Lesion Platform, including the "
                "prediction endpoint, image upload process, probability score, failed uploads, "
                "workflow review, governance, and safety limitations.\n\n"
                "I cannot provide diagnosis, treatment advice, or clinical interpretation of skin lesions."
            ),
        }

        return answers.get(intent, answers["general_platform_support"])

    def _sources_for_intent(self, intent: str) -> List[str]:
        source_map = {
            "api_support": [
                "src/api/routes.py",
                "src/services/prediction_service.py",
                "docs/api.md",
            ],
            "image_upload_support": [
                "src/api/routes.py",
                "docs/api.md",
            ],
            "failed_upload_support": [
                "src/api/routes.py",
                "src/services/prediction_service.py",
                "docs/api.md",
            ],
            "prediction_explanation": [
                "src/schemas/prediction.py",
                "governance/medical_ai_safety_policy.md",
            ],
            "governance": [
                "governance/action_tier_model.md",
                "governance/classification_canon.md",
                "governance/human_in_the_loop_policy.md",
                "governance/medical_ai_safety_policy.md",
            ],
            "general_platform_support": [
                "README.md",
                "copilot_studio/README.md",
            ],
        }

        return source_map.get(intent, source_map["general_platform_support"])

    def _risk_level_for_intent(self, intent: str) -> str:
        if intent in {"prediction_explanation", "governance"}:
            return "Medium"

        return "Low"

    def _medical_refusal(self) -> Dict:
        return {
            "answer": (
                "I can help with technical questions about the Skin Lesion Platform, including "
                "the API, upload flow, prediction response format, governance process, and safety controls.\n\n"
                "I cannot interpret a lesion, confirm whether it is cancer, decide whether it is benign "
                "or malignant, or recommend treatment. For medical concerns, please speak with a "
                "qualified clinician."
            ),
            "intent": "medical_advice",
            "risk_level": "Prohibited",
            "automation_allowed": False,
            "escalation_required": True,
            "sources": [
                "governance/medical_ai_safety_policy.md",
                "governance/action_tier_model.md",
                "governance/human_in_the_loop_policy.md",
            ],
            "safety_note": (
                "Medical diagnosis, lesion interpretation, and treatment advice are outside "
                "the agent's allowed scope."
            ),
        }
