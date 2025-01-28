from flask import (Flask, render_template, request, 
                   jsonify, session, redirect, 
                   url_for)
from DbConnection import PostgresConnection
from forms import LoginForm
from django.contrib.auth.hashers import check_password
import django
import os
import sys
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from django.core.files import File
import datetime


load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/backend/flask_file_uploads'

ALLOWED_EXTENSIONS = {'txt', 'csv'}


def allowed_file(filename):
  return '.' in filename and \
          filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend')
django.setup()


def login_required(f):
  def wrapper(*args, **kwargs):
    if 'username' not in session:
      return redirect(url_for("login"))
    return f(*args, **kwargs)
  wrapper.__name = f.__name__
  return wrapper


@app.route("/", methods=["GET", "POST"])
def home():
  return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
  form = LoginForm(request.form)
  conn = PostgresConnection()
  cursor = conn.cursor()

  if request.method == "POST" and form.validate():
    username = form.username.data
    password = form.password.data
    cursor.execute("""SELECT username, password, is_superuser FROM auth_user WHERE username=%s""", (username,))
    result = cursor.fetchone()
    db_username = result[0]
    db_password = result[1]
    db_is_superuser = result[2]
    if check_password(password, db_password) and db_is_superuser == True:
      session['username'] = username
      return jsonify({'message': 'Login successful'}), 200
    else:
      return jsonify({'error': 'Invalid username or password'}), 401
  return render_template("login.html", form=form)


@app.route("/logout", methods=["GET", "POST"])
def logout():
  session.pop('username', None)
  return jsonify({'message': 'Logged out successfully'}), 200


@app.route("/protected", methods=["GET", "POST"])
@login_required
def protected():
  conn = PostgresConnection()
  cursor = conn.cursor()
  if request.method == "POST":
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for("home"))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        django_file = File(file)
        try:
          cursor.execute("INSERT INTO app1_flaskfiles (filename, filename_data, uploaded_at) VALUES (%s, %s, %s)", 
                        (file.filename, file.filename, datetime.datetime.now()))
          conn.commit()
        except Exception as e:
          conn.rollback()
          return jsonify({"error": str(e)}), 500
        return redirect(url_for('home'))
  return render_template("protected.html")



if __name__ == "__main__":
  app.secret_key = os.getenv("FLASK_SECRET_KEY")
  app.run(debug=True)