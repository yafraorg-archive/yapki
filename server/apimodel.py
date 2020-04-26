from typing import List

from pydantic import BaseModel


class CertBase(BaseModel):
    serialnumber: int
    description: str = None


class CertCreate(CertBase):
    pass


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: int
