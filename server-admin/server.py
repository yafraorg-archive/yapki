from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import uvicorn
import logging

from api.admin import apirouter
from utils.database import SessionLocal, engine, get_db
from model.token import Token
from model import db
from utils.security import create_access_token
from control.usermanagement import authenticate_user

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = FastAPI()

app.include_router(apirouter, tags=["admin"])


@app.on_event("startup")
def startup_event():
    logging.info('start and setup database')
    db.Base.metadata.create_all(bind=engine)
    my_db: Session = SessionLocal()
    # list all users on startup
    my_db.close()


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
