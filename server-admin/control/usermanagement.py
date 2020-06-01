from sqlalchemy.orm import Session

from utils import security
from model import user
from model.db import DbUser


def get_user(db: Session, user_id: int):
    return db.query(DbUser).filter(DbUser.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(DbUser).filter(DbUser.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DbUser).offset(skip).limit(limit).all()


def create_user(db: Session, user: user.UserCreate):
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
