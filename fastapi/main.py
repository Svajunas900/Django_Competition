from fastapi import FastAPI
import uvicorn
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from SqlDbConnection import SqlDbConnection
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  

driver = webdriver.Chrome(options=chrome_options)
app = FastAPI()
sql_connection = SqlDbConnection()
url = ""

driver.get(url)


def get_session():
    with Session(sql_connection) as session:
        yield session 


SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/active_competition")
def get_active_competition(session: SessionDep):
    return json.dumps({"Hello": "World"})


@app.get("/closed_competition")
def get_closed_competition(session: SessionDep):
    return json.dumps({"Hello": "World"})


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=7000)