from sqlalchemy.orm import Session
from OpenAQDataPlatform.app.models.models import Source
from abstract_repository import BaseRepository

class SourceRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def query_by_name_and_id_or_create(
        self, name, id, **kwargs
    ):
        return (
            self.session.query(Source)
            .filter_by(source_name=name)
            .filter_by(source_id=id)
            .first()
            or Source(source_name=name, source_id=id, **kwargs)
        )

    def query_by_name_or_create(self, name, **kwargs):
        return (
            self.session.query(Source)
            .filter_by(source_name=name)
            .first()
            or Source(source_name=name, **kwargs)
        )

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