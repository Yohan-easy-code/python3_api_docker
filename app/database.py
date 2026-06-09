from sqlmodel import create_engine, SQLModel
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if database_url is None:
    raise ValueError("DATABASE_URL is not defined")

engine = create_engine(database_url, echo=True)
