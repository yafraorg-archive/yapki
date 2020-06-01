from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

from utils.database import Base


class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(250), unique=True, index=True)
    hashed_password = Column(String(10000))
    is_active = Column(Boolean, default=True)


class DbCertificate(Base):
    __tablename__ = "certificate"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(256), index=True)
    expdate = Column(DateTime, index=True)
    revdate = Column(DateTime, index=False)
    serial = Column(Integer, index=True)
    file = Column(String(4096), index=False)
    common_name = Column(String(1024), index=True)
    description = Column(Text, index=False)
    valid = Column(Boolean, index=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("DbUser", back_populates="certificate")