from OpenAQDataPlatform.app.models.orm import Source
from OpenAQDataPlatform.app.repostiories.abstract_repository import AbstractRepository


class SourceRepository(AbstractRepository):
    
    def __init__(self) -> None:
        super().__init__()
        
    def create_entry(self, source:Source)->str:
        return super().create_entry()
    
    def get(self, source:Source)->str:
        return super().get()
    
    def update(self, source:Source)->str:
        return super().get()