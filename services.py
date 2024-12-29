from fastapi import APIRouter

user_router = APIRouter()
org_router = APIRouter()
service_router = APIRouter()

@user_router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Urvil Panchal"}, {"Role": "Data Scientist"}]

@org_router.get("/user-org",tags=["ORG"])
async def get_user_org():
    return {'ORG':'Good Org'}

@service_router.get("/service",tags=["Services"])
async def Services():
    return {'This':"is Service Router"}
# app.include_router(router)