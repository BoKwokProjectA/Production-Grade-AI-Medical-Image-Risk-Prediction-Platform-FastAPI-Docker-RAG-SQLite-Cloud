"""
Support service for the Skin Lesion Platform Copilot Studio agent.

The agent answers technical/support questions only. It should never diagnose
a lesion, interpret an uploaded image, or suggest treatment.
"""

from typing import Dict, List, Optional


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
            "should i worry",
            "is this serious",
        ]

    def answer_question(
        self,
        question: str,
        conversation_id: Optional[str] = None,
        user_role: Optional[str] = "user",
    ) -> Dict:
        clean_question = (question or "").strip()
        intent = self._classify_intent(clean_question)

        if intent == "medical_advice":
            return self._medical_refusal()

        return {
            "answer": self._build_answer(intent),
            "intent": intent,
            "risk_level": self._risk_level_for_intent(intent),
            "automation_allowed": self._automation_allowed_for_intent(intent),
            "escalation_required": self._escalation_required_for_intent(intent),
            "sources": self._sources_for_intent(intent),
            "safety_note": (
                "This agent provides technical support for the Skin Lesion Platform only. "
                "It does not provide medical diagnosis, treatment advice, or clinical "
                "interpretation of uploaded images."
            ),
        }

    def _classify_intent(self, question: str) -> str:
        q = question.lower()

        if any(term in q for term in self.medical_terms):
            return "medical_advice"

        if any(term in q for term in ["failed", "fail", "error", "troubleshoot", "400", "500", "reject"]):
            return "failed_upload_support"

        if any(term in q for term in ["upload", "image file", "file type", "multipart", "form-data"]):
            return "image_upload_support"

        if any(term in q for term in ["endpoint", "api", "predict", "/predict", "request", "response"]):
            return "api_support"

        if any(term in q for term in ["probability", "score", "confidence", "risk score"]):
            return "prediction_explanation"

        if any(term in q for term in ["govern", "governance", "safety", "limitation", "human review", "audit", "action tier"]):
            return "governance"

        return "general_platform_support"

    def _build_answer(self, intent: str) -> str:
        answers = {
            "api_support": (
                "The prediction endpoint accepts an uploaded skin lesion image, validates the file, "
                "runs the image through the backend inference pipeline, and returns structured "
                "prediction metadata such as probability, prediction label, model version, and timestamp.\n\n"
                "The output should be treated as a technical model signal for platform workflow support, "
                "not as a medical diagnosis."
            ),
            "image_upload_support": (
                "To upload an image, send the file to the prediction endpoint using a multipart/form-data "
                "request. The backend should validate that the uploaded file is an image before passing it "
                "to the prediction pipeline.\n\n"
                "This is a technical upload process only. The agent must not interpret the uploaded image medically."
            ),
            "failed_upload_support": (
                "A failed upload is usually caused by one of these issues:\n\n"
                "- the request was not sent as multipart/form-data\n"
                "- the uploaded file was not recognised as an image\n"
                "- the wrong endpoint URL was used\n"
                "- the request field name did not match the API contract\n"
                "- the backend service was unavailable or returned an internal error\n\n"
                "Check the request format first, then confirm the endpoint health, then review backend logs."
            ),
            "prediction_explanation": (
                "The probability value is the model's numerical risk signal for the uploaded image. "
                "It should not be treated as a diagnosis.\n\n"
                "A higher probability can support workflow prioritisation or human review, but it must not "
                "be used to tell a user that they do or do not have a medical condition."
            ),
            "governance": (
                "The platform is governed through safety rules, action tiers, human review, and clear limits "
                "on automation.\n\n"
                "Low-risk technical support can be automated. Medium-risk uncertainty should be routed for "
                "review. High-risk or prohibited requests, such as diagnosis, treatment advice, or medical "
                "image interpretation, must be refused."
            ),
            "general_platform_support": (
                "I can help with technical questions about the Skin Lesion Platform, including the prediction "
                "endpoint, image upload process, probability score, failed uploads, governance, and safety limitations.\n\n"
                "I cannot provide diagnosis, treatment advice, or clinical interpretation of skin lesions."
            ),
        }

        return answers.get(intent, answers["general_platform_support"])

    def _sources_for_intent(self, intent: str) -> List[str]:
        source_map = {
            "api_support": [
                "prediction_endpoint.pdf",
                "README.pdf",
            ],
            "image_upload_support": [
                "upload_image.pdf",
                "failed_upload.pdf",
            ],
            "failed_upload_support": [
                "failed_upload.pdf",
                "upload_image.pdf",
            ],
            "prediction_explanation": [
                "probability.pdf",
                "medical_ai_safety_policy.pdf",
            ],
            "governance": [
                "governance.pdf",
                "action_tier_model.pdf",
                "human_in_the_loop_policy.pdf",
                "medical_ai_safety_policy.pdf",
            ],
            "general_platform_support": [
                "README.pdf",
                "knowledge_source_manifest.pdf",
            ],
        }

        return source_map.get(intent, source_map["general_platform_support"])

    def _risk_level_for_intent(self, intent: str) -> str:
        if intent in {"prediction_explanation", "governance"}:
            return "Medium"

        if intent == "medical_advice":
            return "Prohibited"

        return "Low"

    def _automation_allowed_for_intent(self, intent: str) -> bool:
        return intent != "medical_advice"

    def _escalation_required_for_intent(self, intent: str) -> bool:
        return intent == "medical_advice"

    def _medical_refusal(self) -> Dict:
        return {
            "answer": (
                "I cannot provide medical advice or diagnose any skin condition. "
                "Please consult a qualified dermatologist."
            ),
            "intent": "medical_advice",
            "risk_level": "Prohibited",
            "automation_allowed": False,
            "escalation_required": True,
            "sources": [
                "medical_ai_safety_policy.pdf",
                "medical_safety.pdf",
                "action_tier_model.pdf",
            ],
            "safety_note": (
                "Medical diagnosis, lesion interpretation, and treatment advice are outside "
                "the allowed scope of this support agent."
            ),
        }
