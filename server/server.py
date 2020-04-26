from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .api import admin
from .database import SessionLocal, engine, Base


app = FastAPI()

app.include_router(admin.router, tags=["admin"])


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    # list all users on startup
    db.close()

