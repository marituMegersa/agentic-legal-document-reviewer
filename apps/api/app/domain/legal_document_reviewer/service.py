from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.legal_document_reviewer.models import AgenticLegalDocumentReviewerSession, AgenticLegalDocumentReviewerItem
from app.domain.legal_document_reviewer.schemas import AgenticLegalDocumentReviewerSessionCreate, AgenticLegalDocumentReviewerItemCreate

class AgenticLegalDocumentReviewerService:
    @staticmethod
    def create_session(db: Session, data: AgenticLegalDocumentReviewerSessionCreate) -> AgenticLegalDocumentReviewerSession:
        db_obj = AgenticLegalDocumentReviewerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticLegalDocumentReviewerSession:
        return db.query(AgenticLegalDocumentReviewerSession).filter(AgenticLegalDocumentReviewerSession.id == session_id).first()
