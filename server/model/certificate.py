from typing import List
from pydantic import BaseModel


class Certificate(BaseModel):
    id: int
    type: str
    expdate: int
    revdate: int
    serial: int
    file: str
    common_name: str
    description: str = None
    valid: bool
    owner_id: int

