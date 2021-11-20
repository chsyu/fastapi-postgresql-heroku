from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgres://dgxnvlkpkrpuns:8f7a92153206032825c110c47a42c0b94a2c7b2fe2c65fb2f0afe52259587d24@ec2-54-145-9-12.compute-1.amazonaws.com:5432/df52nh7r70gr82"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()