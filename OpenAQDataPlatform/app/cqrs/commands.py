from OpenAQDataPlatform.app.repostiories import source_repository, location_repository, measurement_repository
from OpenAQDataPlatform.app.models.orm import Source, Location, Measurement

def create_source(model:Source):
    return source_repository.get_or_create(model)

def create_location(model:Location):
    return location_repository.get_or_create(model)

def create_measurement(model:Measurement):
    return measurement_repository.get_or_create(model)

def update_source(model:Source, **kwargs):
    source_repository.update(model, **kwargs)

def update_location(model:Location, **kwargs):
    location_repository.update(model, **kwargs)

def update_measurement(model:Measurement, **kwargs):
    measurement_repository.update(model, **kwargs)

def delete_source(model:Source):
    source_repository.delete(model)

def delete_location(model:Location):
    location_repository.delete(model)

def delete_measurement(model:Measurement):
    measurement_repository.delete(model)