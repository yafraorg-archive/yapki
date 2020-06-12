from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text, LargeBinary
from sqlalchemy.orm import relationship

from utils.database import Base


class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(250), unique=True, index=True)
    hashed_password = Column(String(10000))
    public_key = Column(LargeBinary, index=False)
    role = Column(Integer, index=False)
    is_active = Column(Boolean, default=True)


class DbCertificate(Base):
    __tablename__ = "certificate"

    id = Column(Integer, primary_key=True, index=True)
    usage = Column(Integer, index=True)
    type = Column(String(10), index=True)
    expdate = Column(DateTime, index=True)
    revdate = Column(DateTime, index=False)
    serial = Column(String(1024), index=True)
    file = Column(String(1024), index=False)
    common_name = Column(String(1024), index=False)
    distinguished_name = Column(Text, index=False)
    email = Column(String(256), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("DbUser", back_populates="certificate")