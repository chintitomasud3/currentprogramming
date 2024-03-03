from pydantic import BaseModel
class Dbuser(BaseModel):
    Dbuser: str
    password: str