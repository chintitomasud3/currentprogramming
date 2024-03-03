from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Create SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session factory for ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Pydantic model for user data
class Dbuser(BaseModel):
    Dbuser: str
    pasword: str

# FastAPI application instance
app = FastAPI()

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World padmabank"}

# Endpoint to create a new user
@app.post("/createuser")
async def createuser(db:Dbuser):
    return {"message": "Masud New user is created"}