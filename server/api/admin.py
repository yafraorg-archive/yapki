from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..model import apimodel

apirouter = APIRouter()


@apirouter.get("/list/", response_model=List[apimodel.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    """
    Read all the items. Doesn't need authentication.
    """
    items = crud.get_items(db, skip=skip, limit=limit)
    return items