from models import DocumentStatus
from pydantic import BaseModel,  ConfigDict
from uuid import UUID
class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    original_filename : str
    status: DocumentStatus
    file_size: int