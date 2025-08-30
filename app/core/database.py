from sqlmodel import create_engine, SQLModel, Session
from fastapi import Depends
from typing import Annotated


sqlite_file_name = "test.db"
sqlite_url = f"sqlite:///${sqlite_file_name}"
connect_args = {"check_same_thread":False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        return session
    
sesssionDep = Annotated[Session,Depends(get_session)]