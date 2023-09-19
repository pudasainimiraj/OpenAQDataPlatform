import abc
from typing import Union

from OpenAQDataPlatform.app.repostiories.abstract_repository import AbstractRepository
from OpenAQDataPlatform.app.repostiories.location_repository import LocationRepository
from OpenAQDataPlatform.app.repostiories.source_repository import SourceRepository


class AbstractUnitOfWork(abc.ABC):
    def __init__(self)->None:
        self.repo_instance:Union[AbstractRepository,LocationRepository, SourceRepository]
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