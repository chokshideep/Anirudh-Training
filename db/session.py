from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(SQLALCHEMY_DATABASE_URL)

"""ssl_args = {
    'ssl': {
        'ssl_ca': "/ca-cert.crt",
        'ssl_mode': "REQUIRED"
        
    }
}"""


engine = create_engine(SQLALCHEMY_DATABASE_URL) # connect_args=ssl_args  -> ADD THIS IF SSL IS NEEDED

print(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

