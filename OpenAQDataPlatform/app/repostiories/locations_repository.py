from sqlalchemy.orm import Session
from OpenAQDataPlatform.app.repostiories.base_repository import BaseRepository
from OpenAQDataPlatform.app.models.orm import locations

class locationsRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)
    
    def get_or_create(self, model:locations):
        # Check if a locations already exists with the given composite key
        existing_locations = self.session.query(locations).filter_by(
            locations_id=model.locations_id
        ).first()
        
        # If it exists, return the existing locations
        if existing_locations:
            return existing_locations

        # Otherwise, create a new locations
        new_locations = locations(
            locations_id=model.locations_id,
            locations_name=model.locations_name,
            city=model.city, 
            country=model.country, 
            latitude=model.latitude, 
            longitude=model.longitude, 
            count=model.count
        )
        self.session.add(new_locations)
        return new_locations
    
    def get_or_create_batch(self, model_list:list):
        for model in model_list:
            self.get_or_create(model)

    def update(self, model:locations, **kwargs):
        self.session.query(locations).filter_by(locations_id=model.locations_id).update(kwargs)
        
    def query_by_id(self, id:str):
        return self.session.query(locations).filter_by(locations_id=id).first()
    
    def query_all(self):
        return self.session.query(locations).all()
    
    def query(self):
        return self.session.query(locations)

    def delete(self, model:locations):
        self.session.delete(model)
    
    @property
    def model(self):
        return locations

