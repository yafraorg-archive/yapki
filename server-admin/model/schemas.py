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
# YAPKI object model certificate
from typing import List
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel


class Certificate(BaseModel):
    id: int
    usage: int
    state: str
    expdate: datetime
    revdate: datetime = 0
    serial: str
    file: str
    common_name: str
    email: str
    distinguished_name: str
    owner_id: int

    class Config:
        orm_mode = True

    @classmethod
    def shortname(cls):
        return cls.common_name



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: int



class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
