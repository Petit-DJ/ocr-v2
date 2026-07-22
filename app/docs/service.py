from fastapi import UploadFile
from app.storage.service import StorageService



class DocumentService:
    def __init__(self):
        self.storage_service = StorageService()
        
    async def upload_file(self, file: UploadFile):
        file_path = await self.storage_service.save(file)
        return file_path