# Desc: This file is used to import all the repositories in the app
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from OpenAQDataPlatform.app.models.orm import Base
from .locations_repository import locationsRepository
from .measurement_repository import MeasurementRepository
from .source_repository import SourceRepository
from sqlalchemy.orm import sessionmaker

load_dotenv()  # Load environment variables once, outside of the class

TSDB_URI = os.getenv("TSDB_URI")
SessionLocal = sessionmaker(bind=create_engine(TSDB_URI, isolation_level="READ COMMITTED", echo=True))

Base.metadata.create_all(bind=SessionLocal().get_bind())

source_repository:SourceRepository = SourceRepository(SessionLocal())
locations_repository:locationsRepository = locationsRepository(SessionLocal())
measurement_repository:MeasurementRepository = MeasurementRepository(SessionLocal())