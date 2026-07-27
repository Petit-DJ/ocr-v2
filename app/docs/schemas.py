#app/docs/schemas.py

from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.docs.models import DocumentStatus


class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    original_filename : str
    status: DocumentStatus
    file_size: int