from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base



sqlite_file_name = "flask_users.db"
sqlite_url = f'sqlite:///{sqlite_file_name}'


class SqlDbConnection:
  _instance = None
  
  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super().__new__(cls, *args, **kwargs)
      cls._instance = create_engine(f'{sqlite_url}')
      return cls._instance


engine = SqlDbConnection()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)