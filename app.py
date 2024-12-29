from fastapi import FastAPI 
from services import user_router , org_router, service_router


app = FastAPI()
app.include_router(user_router)
app.include_router(org_router)
app.include_router(service_router)

@app.post("/greet")
def Greet(name:str):
    return f"Hello {name}"

@app.get("/name")
def Name():
    return "Hello World"