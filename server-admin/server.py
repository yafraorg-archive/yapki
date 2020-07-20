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
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import uvicorn
import logging
import time

from api.admin import apirouter
from utils.database import SessionLocal, engine, get_db
from model.schemas import Token
from model import db
from utils.security import create_access_token
from control.usermanagement import authenticate_user

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(apirouter, tags=["admin"])


@app.on_event("startup")
def startup_event():
    logger.info('start and setup database')
    db.Base.metadata.create_all(bind=engine)
    my_db: Session = SessionLocal()
    # list all users on startup
    my_db.close()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.post("/login/access-token", response_model=Token)
def login_access_token(
    my_db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    user = authenticate_user(
        my_db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {
        "access_token": create_access_token(subject=user.id),
        "token_type": "bearer",
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
