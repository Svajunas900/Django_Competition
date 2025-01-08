from sqlmodel import create_engine



sqlite_file_name = "django_info.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


class SqlDbConnection:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      connect_args = {"check_same_thread": False}
      cls._instance = super().__new__(cls, *args, **kwargs)
      cls._instance = create_engine(sqlite_url, connect_args=connect_args)
      return cls._instance
    

