from sqlalchemy import Column, Integer,String
from database import Base

class Dbuser(Base):
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    address=Column(String)    