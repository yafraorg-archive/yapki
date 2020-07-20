# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
#  Copyright 2020 yafra.org
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------
#
# YAPKI SQLAlchemy Models
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text, LargeBinary
from sqlalchemy.orm import relationship

from utils.database import Base


class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(250), unique=True, index=True)
    hashed_password = Column(String(2048))
    public_key = Column(String(2048), index=False)
    role = Column(Integer, index=False)
    is_active = Column(Boolean, default=True)

    certificate = relationship("DbCertificate", back_populates="owner")


class DbCertificate(Base):
    __tablename__ = "certificate"

    id = Column(Integer, primary_key=True, index=True)
    usage = Column(Integer, index=True)
    state = Column(String(10), index=True)
    expdate = Column(DateTime, index=False)
    revdate = Column(DateTime, index=False)
    serial = Column(String(1024), unique=True, index=True)
    file = Column(String(1024), index=False)
    common_name = Column(String(1024), index=False)
    email = Column(String(256), index=False)
    distinguished_name = Column(String(2048), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("DbUser", back_populates="certificate")


class DbRequest(Base):
    __tablename__ = "request"

    id = Column(Integer, primary_key=True, index=True)
    request = Column(String(1024), index=False)
    date = Column(DateTime, index=False)
    state = Column(Integer, index=False)
