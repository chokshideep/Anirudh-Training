from fastapi import APIRouter
from apis.version_1 import router_organization


api_router = APIRouter()

tags_metadata = [
    {
        "name": "Organization",
        "description": "API related tto the Organization"
    }
]

api_router.include_router(router_organization.router, prefix='/v1/organization', tags=["Organization"])