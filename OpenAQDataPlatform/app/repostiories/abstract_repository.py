from abc import ABC, abstractmethod
from cassandra import cluster
from cassandra.cqlengine import models

class AbstractRepository(ABC):
    
    def set_cassandra_session(self, models):
        return "Not implemented error"
    
    def create_entry(self):
        return "Not implemented error"
    
    def get(self):
        return "Not implemented error"
    
    def update(self):
        return "Not implemented error"
    
    def delete(self):
        return "Not implemented error"