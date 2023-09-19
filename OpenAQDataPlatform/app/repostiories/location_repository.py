from typing import List

from OpenAQDataPlatform.app.repostiories.abstract_repository import AbstractRepository

from OpenAQDataPlatform.app.models.orm import Location, Mesurement, Source
class LocationRepository(AbstractRepository):
    
    """The methods needs implementation
    """
    def __init__(self):
        pass
    
    
    def create_entry(self, location:Location):
        return super().create_entry()
    
    def get(self):
        return super().get()
    
    def update(self):
        return super().update()
    
    def delete(self):
        return super().delete()