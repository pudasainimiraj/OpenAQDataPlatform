from typing import List
from sqlalchemy.orm import Session
from OpenAQDataPlatform.app.models.orm import Source
from OpenAQDataPlatform.app.repostiories.base_repository import BaseRepository

class SourceRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_or_create(self,model:Source)->Source:
        if model.source_id == None:
            return None
        
        existing_source = self.session.query(Source).filter_by(source_id=model.source_id).first()
        
        if existing_source:
            return existing_source
        
        self.session.add(model)
        return model

    def update(self, model:Source, **kwargs):
        self.session.query(Source).filter_by(source_id=model.source_id).update(kwargs)
        self.session.commit()
        
    def query_by_id(self, id:str)->Source:
        return self.session.query(Source).filter_by(source_id=id).first()
    
    def query_all(self)->List[Source]:
        return self.session.query(Source).all()
    
    def query(self):
        return self.session.query(Source)

    def delete(self, model:Source):
        self.session.delete(model)
        self.session.commit()
    
    @property
    def model(self):
        return Source