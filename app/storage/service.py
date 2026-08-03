#app/storage/service.py
# from sqlalchemy.orm import Session
from pathlib import Path

from fastapi import UploadFile

from app.core.config import UPLOAD_DIR


UPLOAD_DIR = Path(UPLOAD_DIR)  # from config, e.g. "app/uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

class StorageService:
    async def save(self, file: UploadFile) -> str:
       file_path = UPLOAD_DIR / file.filename
       contents = await file.read()
       with open(file_path, "wb") as f:
                   f.write(contents)
       return str(file_path)
