from uuid import UUID

from sqlalchemy.orm import Session

from models import DbDoc


class DocumentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, document: DbDoc) -> DbDoc:
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def get_doc_by_id(self, id: UUID) -> DbDoc | None:
        return self.db.query(DbDoc).filter(DbDoc.id == id).first()