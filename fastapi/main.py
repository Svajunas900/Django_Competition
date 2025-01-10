from fastapi import FastAPI
import uvicorn
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from SqlDbConnection import SqlDbConnection
import json
from datetime import datetime, timedelta, timezone
from functions import find_competitions
# from pydantic import BaseModel
from passlib.context import CryptContext
# from jwt.exceptions import InvalidTokenError


app = FastAPI()
sql_connection = SqlDbConnection()


def get_session():
    with Session(sql_connection) as session:
        yield session 


# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
SessionDep = Annotated[Session, Depends(get_session)]
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None


# class UserInDB(User):
#     hashed_password: str


# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return pwd_context.hash(password)


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)


# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now(timezone.utc) + expires_delta
#     else:
#         expire = datetime.now(timezone.utc) + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt






















@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/active_competition")
def get_active_competition(session: SessionDep):
    active_competitions = {}
    competitions = find_competitions()
    date_format = "%b. %d, %Y, %I:%M %p"  
    for key, value in competitions.items():
        date_string = value[1].replace('a.m.', 'AM').replace('p.m.', 'PM')
        end = datetime.strptime(date_string, date_format)   
        if end > datetime.now():
            active_competitions[key] = [value]
    return json.dumps(active_competitions)


@app.get("/closed_competition")
def get_closed_competition(session: SessionDep):
    closed_competitions = {}
    competitions = find_competitions()
    date_format = "%b. %d, %Y, %I:%M %p"  
    for key, value in competitions.items():
        date_string = value[1].replace('a.m.', 'AM').replace('p.m.', 'PM')
        end = datetime.strptime(date_string, date_format)   
        if end < datetime.now():
            closed_competitions[key] = value
    return json.dumps(closed_competitions)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80)