from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL = "postgresql:psycopg2://soriat_user:Xu1MG6MsyoFDheiliSUwVRprNGVODOoY@dpg-dc3h77brjlhs73frsme0-a.virginia-postgres.render.com/soriat"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
