from fastapi import FastAPI
import uvicorn
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from SqlDbConnection import SqlDbConnection
import json
from datetime import datetime
from functions import find_competitions
from passlib.context import CryptContext


app = FastAPI()
sql_connection = SqlDbConnection()


def get_session():
    with Session(sql_connection) as session:
        yield session 


SessionDep = Annotated[Session, Depends(get_session)]
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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