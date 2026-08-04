#app/docs/service.py

from pathlib import Path

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.docs.models import DbDoc, DocumentStatus
from app.docs.repository import DocumentRepository
from app.storage.service import StorageService
from app.processing.pipeline import process_document

class DocumentService:
    def __init__(self, db: Session):
        self.storage_service = StorageService()
        self.repository = DocumentRepository(db)
        
    async def upload_file(self, file: UploadFile):
        file_path = await self.storage_service.save(file)
        try:
            extracted_text = process_document(file_path)
            status = DocumentStatus.COMPLETED
        except Exception:
            extracted_text = None
            status = DocumentStatus.FAILED

        document = DbDoc(
            original_filename = file.filename,
            stored_filename = Path(file_path).name,
            content_type = file.content_type,
            status = DocumentStatus.UPLOADED,
            file_size = Path(file_path).stat().st_size,
            extracted_text = extracted_text,
            # created_at = datetime.utcnow,    
        )
        document = self.repository.create(document)

        return document