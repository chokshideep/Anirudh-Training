from typing import Optional
from pydantic import BaseModel


class UserCreateModel(BaseModel):
    name: str
    mail_id: str
    password: str
