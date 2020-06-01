from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.database import get_db
from model.certificate import Certificate

apirouter = APIRouter()


@apirouter.get("/list/", response_model=List[Certificate])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Read all the items. Doesn't need authentication.
    """
    return "x"
