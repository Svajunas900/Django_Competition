from flask import Flask, render_template, flash, redirect, url_for, request
import jwt
from forms import RegistrationForm
import os 
from SqliteDbConnection import db_session
from models import FlaskUser
from datetime import timezone, timedelta, datetime

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


try:
    os.makedirs(app.instance_path)
except OSError:
    pass




@app.route("/")
def home():
  return ""


@app.route("/login", methods=["GET", "POST"])
def login():
  return render_template('login.html')


@app.route("/register", methods=["GET", "POST"])
def register():
  form = RegistrationForm(request.form)
  print(form.username.data, form.email.data, form.password.data)
  print(form.validate())
  if request.method == 'POST' and form.validate():
      print("Hello")
      name = form.username.data
      email = form.email.data
      password = form.password.data
      expiration_time = datetime.now(tz=timezone.utc) + timedelta(hours=12)
      payload = {"exp": expiration_time}
      token = jwt.encode(payload=payload, key="My_Secret")
      print(expiration_time, token)
      user = FlaskUser(name, email, password, token, expiration_time)
      print("suscces")
      db_session.add(user)
      db_session.commit()
      flash('Thanks for registering')
      return redirect(url_for('login'))
  return render_template('register.html', form=form)


print(FlaskUser.query.all())