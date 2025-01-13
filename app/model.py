from sqlalchemy import Boolean, Column, Integer, String
from database import Base
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    
    