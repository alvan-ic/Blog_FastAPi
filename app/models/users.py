from sqlmodel import SQLModel, Field


class User(SQLModel,table=True):
    id: int| None = Field(default=None, primary_key=True)
    first_name: str = Field(index=True,max_length=255)
    last_name: str 
    email: str 
    password:str
    age:int | None 


