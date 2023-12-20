from sqlalchemy.orm import Session
from abstract_repository import BaseRepository
from OpenAQDataPlatform.app.models.models import Location

class LocationRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def query_by_name_and_id_or_create(
        self, name, id, **kwargs
    ):
        return (
            self.session.query(Location)
            .filter_by(location_name=name)
            .filter_by(location_id=id)
            .first()
            or Location(location_name=name, location_id=id, **kwargs)
        )

    def query_by_name_or_create(self, name, **kwargs):
        return (
            self.session.query(Location)
            .filter_by(location_name=name)
            .first()
            or Location(location_name=name, **kwargs)
        )

    def update(self, model, **kwargs):
        self.session.query(Location).filter_by(location_id=model.location_id).update(kwargs)
        self.session.commit()
        
    def query_by_id(self, id):
        return self.session.query(Location).filter_by(location_id=id).first()
    
    def query_all(self):
        return self.session.query(Location).all()
    
    def query(self):
        return self.session.query(Location)

    def delete(self, model):
        self.session.delete(model)
        self.session.commit()

