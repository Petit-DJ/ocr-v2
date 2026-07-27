#app/docs/router.py

from fastapi import APIRouter, File, UploadFile, Depends
from app.docs.service import DocumentService
from sqlalchemy.orm import Session
from app.db.dependencies import get_db

router = APIRouter (
    prefix = '/docs',
    tags = ['Docs']
    )

document_service = DocumentService(db)


@router.post("/upload")
async def upload_file(
    file: UploadFile=File(...),
    db: Session = Depends(get_db),
    ):

    result = await document_service.upload_file(file)
    return result
