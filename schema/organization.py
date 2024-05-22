from typing import Optional
from pydantic import BaseModel


class OrganizationCreateModel(BaseModel):
    name: str
    mail_id: str
    password: str
