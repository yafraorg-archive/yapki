#! /usr/bin/env python

from sqlalchemy.orm import Session
from utils.database import SessionLocal, engine
from model import db
from control.certlist import certlist
from typing import List
from model.certificate import Certificate

# Test if it works
print("yapki CLI")

certs = List[Certificate]
certs = certlist("../yapki/index.txt")
for item in certs:
    print(f"certificate is {item.json()}")

db.Base.metadata.create_all(bind=engine)
my_db: Session = SessionLocal()
print(engine.table_names())
# list all users on startup
my_db.close()

