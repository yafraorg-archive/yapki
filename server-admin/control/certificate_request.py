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
# YAPKI CLI
from sqlalchemy.orm import Session
from utils.database import SessionLocal, engine
from model.db import DbCertificate, DbUser, DbRequest, Base

def get_user(db: Session, user_id: int):
    return db.query(DbRequest).filter(DbRequest.id == user_id).first()

