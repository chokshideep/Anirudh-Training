from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schema.organization import OrganizationCreateModel
from db.repository.organization import create_organization_logic

router = APIRouter()


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_organization(organization_data: OrganizationCreateModel, db: Session = Depends(get_db)):
    response = create_organization_logic(organization_data, db)
    return response
