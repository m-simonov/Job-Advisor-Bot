from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from sqlalchemy_utils import database_exists, create_database


engine = create_engine(
    DATABASE_URL
)


Session = sessionmaker(engine)
