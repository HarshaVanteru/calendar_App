
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):

    __tablename__ = "Users"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String(100),index=True, unique=True,nullable=False)
    hashed_password = Column(String(100),nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())