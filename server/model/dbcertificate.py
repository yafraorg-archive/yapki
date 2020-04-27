from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from server.database import Base


class DbCertificate(Base):
    __tablename__ = "certificate"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    expdate = Column(DateTime, index=True)
    revdate = Column(DateTime, index=False)
    serial = Column(Integer, index=True)
    file = Column(String, index=False)
    common_name = Column(String, index=True)
    description = Column(String, index=False)
    valid = Column(Boolean, index=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="certificate")
