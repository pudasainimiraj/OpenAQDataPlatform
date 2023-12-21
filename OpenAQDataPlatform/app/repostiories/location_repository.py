from sqlalchemy.orm import Session
from OpenAQDataPlatform.app.repostiories.base_repository import BaseRepository
from OpenAQDataPlatform.app.models.orm import Location

class LocationRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)
    
    def get_or_create(self, model:Location):
        # Check if a location already exists with the given composite key
        existing_location = self.session.query(Location).filter_by(
            location_id=model.location_id
        ).first()
        
        # If it exists, return the existing location
        if existing_location:
            return existing_location

        # Otherwise, create a new location
        new_location = Location(
            location_id=model.location_id,
            location_name=model.location_name,
            city=model.city, 
            country=model.country, 
            latitude=model.latitude, 
            longitude=model.longitude, 
            count=model.count
        )
        self.session.add(new_location)
        self.session.commit()
        return new_location

    def update(self, model:Location, **kwargs):
        self.session.query(Location).filter_by(location_id=model.location_id).update(kwargs)
        self.session.commit()
        
    def query_by_id(self, id:str):
        return self.session.query(Location).filter_by(location_id=id).first()
    
    def query_all(self):
        return self.session.query(Location).all()
    
    def query(self):
        return self.session.query(Location)

    def delete(self, model:Location):
        self.session.delete(model)
        self.session.commit()
    
    @property
    def model(self):
        return Location

