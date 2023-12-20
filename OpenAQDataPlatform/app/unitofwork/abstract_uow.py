import abc
import os
from typing import Union
from dotenv import load_dotenv
from OpenAQDataPlatform.app.repostiories.abstract_repository import BaseRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

load_dotenv()

TSDB_URI = os.getenv("TSDB_URI")

class AbstractUOW(abc.ABC):
    def __init__(self)->None:
        self.repo_instance:Union[BaseRepository, None] = None
        super().__init__()
        
    def __enter__(self)-> "AbstractUnitOfWork":
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.rollback()
        else:
            self.commit()
            
    @abc.abstractmethod
    def commit(self):
        pass
    
    @abc.abstractmethod
    def rollback(self):
        pass

class UnitOfWork(AbstractUOW):
    def __init__(self, repo_instance:BaseRepository)->None:
        self.repo_instance = repo_instance
        self._session = sessionmaker(
                            bind=create_engine(TSDB_URI, isolation_level="READ COMMITTED", echo=True)
                        )
        super().__init__()

    def commit(self):
        try:
            self._session.commit()
        except Exception as e:
            self.rollback()
            raise e
            
        
    def rollback(self):
        self._session.rollback()
    