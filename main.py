from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from typing import Annotated
from sqlmodel import Session, select

from .model import User
from .db_manager import get_session_dependency, generate_tables



# manage app lifetime (started, interrupted, stopped)
@asynccontextmanager
async def app_lifespan(app: FastAPI):
    generate_tables() # on start up(before yield), generate tables
    print("app started")
    yield

# the fastapi app
app = FastAPI(lifespan=app_lifespan)


# ALL SERVICES LISTED BELOW

# get all users
@app.get("/user/")
async def get_users(session: Annotated[Session, Depends(get_session_dependency)]):
    sql_query = select(User)
    result = session.exec(sql_query)
    return result.all()



# create a user
@app.post("/user/")
async def create_user(user: User, session: Annotated[Session, Depends(get_session_dependency)]):
    new_user = user
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"created successfully" : new_user}



# get a user
@app.get("/user/{user_id}")
async def get_a_user(user_id: int, session: Annotated[Session, Depends(get_session_dependency)]):
    user = session.get(User, user_id)
    return {"data": user}



#update a user
@app.put("/user/{user_id}")
async def update_user(user_id: int, new_user: User, session: Annotated[Session, Depends(get_session_dependency)]):
    db_user = session.get(User, user_id)

    db_user.name = new_user.name
    db_user.age = new_user.age
    db_user.adress = new_user.adress

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return {"user data updated" : db_user}



#delete a user
@app.delete("/user/{user_id}")
async def delete_user(user_id: int, session: Annotated[Session, Depends(get_session_dependency)]):
    db_user = session.get(User, user_id)
    if db_user:
        session.delete(db_user)
        session.commit()

    all_data = session.exec(select(User)).all()
    return {"data state": "deleted",
            "new data set" : all_data
            }

