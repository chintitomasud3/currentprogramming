from fastapi import FastAPI
from . import schemas,models

app = FastAPI()

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World padmabank PLC"}

# Endpoint to create a new user
@app.post("/createuser")
async def createuser(db:schemas.Dbuser):
    return {"message": f"Masud New user is created name : {db.Dbuser}"}

@app.get("/experiment")
async def experiment():
    return {"message":"experiment korte hobe"}
