from flask import Flask, render_template
from SqliteDbConnection import SqlDbConnection
import jwt


app = Flask(__name__)
sqlite_connection = SqlDbConnection()


@app.route("/")
def login():
  return ""


@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/register")
def register():
  return render_template('register.html')