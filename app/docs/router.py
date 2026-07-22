from fastapi import APIRouter, File, UploadFile
from app.docs.service import DocumentService
router = APIRouter (
    prefix = '/docs',
    tags = ['Docs']
    )

document_service = DocumentService()


@router.post("/upload")
async def upload_file(file: UploadFile=File(...)):
    result = await document_service.upload_file(file)
    return result
