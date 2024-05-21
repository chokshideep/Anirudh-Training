import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    PROJECT_VERSION = os.getenv("PROJECT_VERSION")

    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    server = os.getenv("D_SERVER")
    database = os.getenv("DB_DATABASE")




settings = Settings()