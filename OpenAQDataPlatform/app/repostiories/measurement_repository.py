from sqlalchemy.orm import Session
from abstract_repository import BaseRepository
from OpenAQDataPlatform.app.models.models import Measurement
from OpenAQDataPlatform.app.models.orm import measurement


class MeasurementRepository(BaseRepository):
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

    def query_by_source_id(self, source_id):
        return self.session.query(Measurement).filter_by(source_id=source_id).all()

    def query_by_location_id(self, location_id):
        return self.session.query(Measurement).filter_by(location_id=location_id).all()

    def query_by_parameter_id(self, parameter_id):
        return self.session.query(Measurement).filter_by(parameter_id=parameter_id).all()

    def query_by_source_id_and_location_id(self, source_id, location_id):
        return self.session.query(Measurement).filter_by(source_id=source_id).filter_by(location_id=location_id).all()

    def query_by_date(self, start_date, end_date):
        return self.session.query(Measurement).filter(measurement.c.date >= start_date).filter(measurement.c.date <= end_date).all()

    def query_by_value(self, value):
        return self.session.query(Measurement).filter_by(value=value).all()
    
    def query_by_parameter(self, parameter):
        return self.session.query(Measurement).filter_by(parameter=parameter).all()

    def delete(self, model):
        self.session.delete(model)
        self.session.commit()