from fastapi import UploadFile
from pathlib import Path
class StorageService:
    async def save(self, file: UploadFile) -> str:
    #    file_path =  f"C:/Users/DJSuryansh-BroadwayI/AI_Team/Grad_i/ocr-v2/app/uploads/{file.filename}"
       UPLOAD_DIR = Path("C:/Users/DJSuryansh-BroadwayI/AI_Team/Grad_i/ocr-v2/app/uploads/") 
       file_path = UPLOAD_DIR / file.filename
       contents = await file.read()
       with open(file_path, "wb") as f:
                   f.write(contents)
       return file_path