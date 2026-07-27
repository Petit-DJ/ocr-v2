# app/docs/router.py

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.docs.service import DocumentService

router = APIRouter(prefix="/docs", tags=["Docs"])



@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)):
    
    document_service = DocumentService(db)

    result = await document_service.upload_file(file)
    return result
