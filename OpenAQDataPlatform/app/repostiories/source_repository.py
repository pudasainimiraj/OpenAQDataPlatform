from sqlalchemy.orm import Session
from OpenAQDataPlatform.app.models.orm import Source
from OpenAQDataPlatform.app.repostiories.base_repository import BaseRepository

class SourceRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_or_create_source(self,model):
        if model.source_id == None:
            return self.query_by_name_or_create(model.source_name)
        
        existing_source = self.session.query(Source).filter_by(source_id=model.source_id).first()
        
        if existing_source:
            return existing_source
        
        self.session.add(model)
        return model

    def update(self, model, **kwargs):
        self.session.query(Source).filter_by(source_id=model.source_id).update(kwargs)
        self.session.commit()
        
    def query_by_id(self, id):
        return self.session.query(Source).filter_by(source_id=id).first()
    
    def query_all(self):
        return self.session.query(Source).all()
    
    def query(self):
        return self.session.query(Source)

    def delete(self, model):
        self.session.delete(model)
        self.session.commit()