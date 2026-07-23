from fastapi import APIRouter, File, UploadFile, Depends
from app.docs.service import DocumentService
from sqlalchemy.orm import Session
from app.db.dependencies import get_db

router = APIRouter (
    prefix = '/docs',
    tags = ['Docs']
    )

document_service = DocumentService()


@router.post("/upload")
async def upload_file(file: UploadFile=File(...)):
    result = await document_service.upload_file(file)
    db: Session = Depends(get_db)
    return result
