from fastapi import FastAPI, Query
from typing import Annotated, List

from app.core.database import create_db_and_tables, sesssionDep
from app.models.users import User
from contextlib import asynccontextmanager
from app.services.user import create_user_db, get_users_db

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.post('/users')
def create_user(user: User, session:sesssionDep)-> User:
    return create_user_db(user=user, session=session)

@app.get("/users")
def get_users(
    session:sesssionDep,
    offset:int=0, 
    limit: Annotated[int, Query(le=100)]=100)->List[User]:
    return get_users_db(session=session,offset=offset,limit=limit)


