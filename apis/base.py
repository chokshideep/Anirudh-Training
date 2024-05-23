from fastapi import APIRouter
from apis.version_1 import router_organization, router_user


api_router = APIRouter()

tags_metadata = [
    {
        "name": "Organization",
        "description": "API related to the Organization"
    },
    {
        "name": "User",
        "description": "API related to the User"
    }
]

api_router.include_router(router_organization.router, prefix='/v1/organization', tags=["Organization"])
api_router.include_router(router_user.router, prefix='/v1/organization', tags=["User"])