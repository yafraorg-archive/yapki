from typing import List
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel


class Certificate(BaseModel):
    state: str
    usage: int
    expdate: datetime
    revdate: datetime = 0
    serial: str
    file: str
    common_name: str
    email: str
    distinguished_name: str
    owner_id: int

    @classmethod
    def shortname(cls):
        return cls.common_name