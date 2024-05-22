from fastapi import FastAPI
from core.config import settings
from db.base import Base
from db.session import engine
from apis.base import api_router, tags_metadata


def include_router(app):
    app.include_router(api_router)


def create_table():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION,
                  openapi_tags=tags_metadata)
    print()
    create_table()
    include_router(app)
    return app


app = start_application()
