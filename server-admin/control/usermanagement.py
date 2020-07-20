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
# YAPKI user
from sqlalchemy.orm import Session

from utils import security
from model.schemas import User, UserCreate
from model.db import DbUser


def get_user(db: Session, user_id: int):
    return db.query(DbUser).filter(DbUser.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(DbUser).filter(DbUser.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DbUser).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = security.get_password_hash(user.password)
    db_user = DbUser(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db=db, email=email)
    if not user:
        return None
    if not security.verify_password(password, user.hashed_password):
        return None
    return user
