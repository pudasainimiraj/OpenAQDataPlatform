import abc, os 
from typing import Union
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


load_dotenv()

TSDB_URI = os.getenv("TSDB_URI")
if not TSDB_URI:
    raise ValueError("TSDB_URI environment variable not set")


