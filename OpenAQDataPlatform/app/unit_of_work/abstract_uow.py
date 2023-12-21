import abc
import os
from typing import Union
from dotenv import load_dotenv
from OpenAQDataPlatform.app.models.orm import Source
from OpenAQDataPlatform.app.repostiories import LocationRepository, MeasurementRepository, SourceRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


load_dotenv()  # Load environment variables once, outside of the class

TSDB_URI = os.getenv("TSDB_URI")
SessionLocal = sessionmaker(bind=create_engine(TSDB_URI, isolation_level="READ COMMITTED", echo=True))

class AbstractUOW(abc.ABC):
    def __init__(self) -> None:
        self.repository_object: Union[LocationRepository, MeasurementRepository, SourceRepository]
        super().__init__()
        
    def __enter__(self) -> "AbstractUOW":
        self._session = SessionLocal()  # Create a new session when entering the context
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.rollback()
        else:
            self.commit()
        self._session.close()  # Close the session when exiting the context

    @abc.abstractmethod
    def commit(self):
        pass
    
    @abc.abstractmethod
    def rollback(self):
        pass

class UnitOfWork(AbstractUOW):
    def __init__(self, repository_object: Union[LocationRepository, MeasurementRepository, SourceRepository]):
        self.repository_object = repository_object
        super().__init__()

    def commit(self):
        try:
            self._session.commit()
        except Exception as e:
            self.rollback()
            raise e
        
    def rollback(self):
        self._session.rollback()

