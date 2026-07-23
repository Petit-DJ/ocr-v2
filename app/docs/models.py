#models
from app.db.base import Base
from sqlalchemy.sql.sqltypes import String
from sqlalchemy import Enum, DateTime, Integer
from sqlalchemy.orm import mapped_column, Mapped
import enum
from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy.dialects.postgresql import UUID as PGUUID


class DocumentStatus(str, enum.Enum):
    UPLOADED = "UPLOADED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class DbDoc(Base):
    __tablename__ = "documents"

    id: Mapped [UUID] = mapped_column (
        PGUUID(as_uuid=True),
        primary_key= True,
        default = uuid4,
    )

    original_filename: Mapped[str] = mapped_column(String(255))
    stored_filename: Mapped[str] = mapped_column(String(255))
    content_type: Mapped[str] = mapped_column(String(255))
    status: Mapped[DocumentStatus] = mapped_column(
        Enum(DocumentStatus),
        default= DocumentStatus.UPLOADED
        )
    file_size: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default = datetime.utcnow)