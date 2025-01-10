from sqlalchemy import Column, Integer, String, DateTime
from SqliteDbConnection import Base, init_db

class FlaskUser(Base):
    __tablename__ = 'flask_users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120))
    password = Column(String(50))
    token = Column(String(500))
    expiration_time = Column(DateTime())

    def __init__(self, name=None, email=None, password=None, token=None, expiration_time=None):
        self.name = name
        self.email = email
        self.password = password
        self.token = token
        self.expiration_time = expiration_time

    def __repr__(self):
        return f'User: {self.name!r}, token: {self.token}, expiration time: {self.expiration_time}>'
  
init_db()