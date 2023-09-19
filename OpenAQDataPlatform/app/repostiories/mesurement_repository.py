from OpenAQDataPlatform.app.models.orm import Mesurement
from OpenAQDataPlatform.app.repostiories.abstract_repository import AbstractRepository


class MesurementRepository(AbstractRepository):
    
    """The method needs implementation
    """
    def __init__(self) -> None:
        super().__init__()
        
    def create_entry(self, mesurement:Mesurement)->str:
        return super().create_entry()
    
    def get(self, mesurement:Mesurement)->str:
        return super().get()
    
    def update(self,mesurement:Mesurement)->str:
        return super().update()
    
    def delete(self, mesurement:Mesurement)->str:
        return super().delete()