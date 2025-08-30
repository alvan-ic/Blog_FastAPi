from app.models.users import User
from app.core.database import sesssionDep
from fastapi import HTTPException, Query
from sqlmodel import select
from typing import Annotated, List

def create_user_db(user: User, session:sesssionDep)-> User:
    validate_user(user,session)
    session.add(user)
    session.commit()
    session.refresh(user)

    return user

def validate_user(user: User,session:sesssionDep):
    existing_user = session.get(User,user.id)
    if existing_user:
        raise HTTPException(status_code=400, detail=f" user id: {user.id} already exists")
    
    existing_user = session.scalar(select(User).where(User.email == user.email))
    if existing_user:
        raise HTTPException(status_code=400, detail=f"email: {user.email} already exists")

    return 

def get_users_db(
    session:sesssionDep,
    offset:int=0, 
    limit: Annotated[int, Query(le=100)]=100)->List[User]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users

