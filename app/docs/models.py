#models
from app.db.base import Base
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Column


class DbDoc(Base):
    __tablename__ = "documents"
    id = Column (Integer, primary_key= True, index= True)
    filename = Column(String)
    file_path = Column(String)
    status = Column(String)
    created_at = Column()