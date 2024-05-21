from fastapi import FastAPI
from core.config import settings
from db.base import Base
from db.session import engine


def create_table():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    print()
    create_table()
    return app


app = start_application()
