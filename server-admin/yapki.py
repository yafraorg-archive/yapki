from sqlalchemy.orm import Session
from utils.database import SessionLocal, engine
from model import db

# Test if it works
print("yapki CLI")
db.Base.metadata.create_all(bind=engine)
my_db: Session = SessionLocal()
print(engine.table_names())
# list all users on startup
my_db.close()

