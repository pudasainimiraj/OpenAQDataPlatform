from sqlalchemy.orm import Session
from OpenAQDataPlatform.app.repostiories.base_repository import BaseRepository
from OpenAQDataPlatform.app.models.orm import Measurement
from OpenAQDataPlatform.migrations import location

class MeasurementRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_or_create_measurement(self, location_id, parameter, value, unit, date, source_id):
        # Check if a measurement already exists with the given composite key
        existing_measurement = self.session.query(Measurement).filter_by(
            location_id=location_id, 
            parameter=parameter, 
            date=date
        ).first()
        
        # If it exists, return the existing measurement
        if existing_measurement:
            return existing_measurement

        # Otherwise, create a new measurement
        new_measurement = Measurement(
            location_id=location_id, 
            parameter=parameter, 
            value=value, 
            unit=unit, 
            date=date, 
            source_id=source_id
        )
        self.session.add(new_measurement)
        self.session.commit()
        return new_measurement


    def update(self, model, **kwargs):
        self.session.query(Measurement).filter_by(location_id=model.location_id, parameter=model.parameter, date=model.date).update(kwargs)
        self.session.commit()

    def query_all(self):
        return self.session.query(Measurement).all()

    def query(self):
        return self.session.query(Measurement)

    def query_by_source_id(self, source_id):
        return self.session.query(Measurement).filter_by(source_id=source_id).all()

    def query_by_location_id(self, location_id):
        return self.session.query(Measurement).filter_by(location_id=location_id).all()

    def query_by_parameter(self, parameter):
        return self.session.query(Measurement).filter_by(parameter=parameter).all()

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