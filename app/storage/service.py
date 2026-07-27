#app/storage/service.py
# from sqlalchemy.orm import Session
from pathlib import Path

from fastapi import UploadFile


class StorageService:
    async def save(self, file: UploadFile) -> str:
    #    file_path =  f"C:/Users/DJSuryansh-BroadwayI/AI_Team/Grad_i/ocr-v2/app/uploads/{file.filename}"
       UPLOAD_DIR = Path("C:/Users/DJSuryansh-BroadwayI/AI_Team/Grad_i/ocr-v2/app/uploads/") 
       file_path = UPLOAD_DIR / file.filename
       contents = await file.read()
       with open(file_path, "wb") as f:
                   f.write(contents)
       return str(file_path)

#UPLOAD_DIR = Path(settings.UPLOAD_DIR)  # from config, e.g. "app/uploads"
#UPLOAD_DIR.mkdir(parents=True, exist_ok=True)