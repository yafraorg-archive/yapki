#! /usr/bin/env python

from sqlalchemy.orm import Session
from utils.database import SessionLocal, engine
from model.db import DbCertificate, DbUser, Base
from control.certlist import certlist
from typing import List
from model.certificate import Certificate

# Test if it works
print("yapki CLI")

# connect to DB and list all entities
print("yapki CLI - list all entities within database")
Base.metadata.create_all(bind=engine)
my_db: Session = SessionLocal()
print(engine.table_names())


# list all users on startup
print("yapki CLI - USERS")
users = my_db.query(DbUser).order_by(DbUser.email).all()
if users:
    print("yapki CLI - list users already within the database")
    for u in users:
        print(u.email)
else:
    # insert admin user
    print("yapki CLI - insert admin user into database")
    db_user = DbUser(email="ca@nissle.ch", hashed_password="", public_key=0, role=1, is_active=1)
    my_db.add(db_user)
    my_db.commit()
    my_db.refresh(db_user)

# list all certs
print("yapki CLI - CERTIFICATE")
certsdb = my_db.query(DbCertificate).order_by(DbCertificate.common_name).all()
if certsdb:
    print("yapki CLI - list all certificates stored in the database")
    for c in certsdb:
        print(c.serial)
else:
    # insert certs which are not yet in the db
    print("yapki CLI - update certificate database")
    certs = List[Certificate]
    certs = certlist("../yapki/index.txt")
    for item in certs:
        print(f"certificate is {item.json()}")
        db_cert = DbCertificate(usage=item.usage, state=item.state, expdate=item.expdate, revdate=item.revdate,
                                serial=item.serial, file=item.file, common_name=item.common_name, email=item.email,
                                distinguished_name=item.distinguished_name, owner_id=1)
        my_db.add(db_cert)
        my_db.commit()
        my_db.refresh(db_cert)



# close db
print("yapki CLI - database close")
my_db.close()
