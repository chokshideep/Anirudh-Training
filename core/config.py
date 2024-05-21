import os
import urllib
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    PROJECT_VERSION = os.getenv("PROJECT_VERSION")

    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_DATABASE")
    driver = "ODBC Driver 18 for SQL Server"

    params = urllib.parse.quote_plus(
        f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

    DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"


settings = Settings()
