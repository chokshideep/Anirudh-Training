from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schema.organization import OrganizationCreateModel
from schema.user import UserCreateModel
from db.repository.organization import create_user_logic

router = APIRouter()


@router.post("/{organization_uuid}/user/create", status_code=status.HTTP_201_CREATED)
async def create_user_organization(organization_uuid: str, user_data: UserCreateModel, db: Session = Depends(get_db)):
    response = create_user_logic(organization_uuid, user_data, db)
    return response
