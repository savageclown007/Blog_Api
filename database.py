from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHAMY_DATABASE = 'sqlite:///blog.db'

engine = create_engine(SQLALCHAMY_DATABASE,connect_args={
    "check_same_thread":False
} )

SessionLocale = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocale()
    try:
        yield db
    finally:
        db.close()
