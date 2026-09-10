from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.legal_document_reviewer.schemas import AgenticLegalDocumentReviewerSessionCreate, AgenticLegalDocumentReviewerSessionResponse
from app.domain.legal_document_reviewer.service import AgenticLegalDocumentReviewerService

router = APIRouter(prefix="/api/v1/legal_document_reviewer", tags=["Agentic Legal Document Reviewer Domain"])

@router.post("/sessions", response_model=AgenticLegalDocumentReviewerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticLegalDocumentReviewerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Legal Document Reviewer.
    """
    return AgenticLegalDocumentReviewerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticLegalDocumentReviewerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticLegalDocumentReviewerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
