from sqlalchemy.orm import Session
from abstract_repository import BaseRepository
from OpenAQDataPlatform.app.models.models import Measurement
from OpenAQDataPlatform.app.models.orm import measurement


class Measurement(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def query_by_name_and_id_or_create(
        self, name, id, **kwargs
    ):
        return (
            self.session.query(Measurement)
            .filter_by(measurement_name=name)
            .filter_by(measurement_id=id)
            .first()
            or Measurement(measurement_name=name, measurement_id=id, **kwargs)
        )

    def query_by_name_or_create(self, name, **kwargs):
        return (
            self.session.query(Measurement)
            .filter_by(measurement_name=name)
            .first()
            or Measurement(measurement_name=name, **kwargs)
        )

    def update(self, model, **kwargs):
        self.session.query(Measurement).filter_by(measurement_id=model.measurement_id).update(kwargs)
        self.session.commit()
        
    def query_by_id(self, id):
        return self.session.query(Measurement).filter_by(measurement_id=id).first()
    
    def query_all(self):
        return self.session.query(Measurement).all()
    
    def query(self):
        return self.session.query(Measurement)

    def delete(self, model):
        self.session.delete(model)
        self.session.commit()