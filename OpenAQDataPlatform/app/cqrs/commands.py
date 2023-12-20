from OpenAQDataPlatform.app.repostiories import source_repository, location_repository, measurement_repository

def create_source(source_name, source_id, **kwargs):
    return source_repository.query_by_name_and_id_or_create(source_name, source_id, **kwargs)

def create_location(location_name, location_id, **kwargs):
    return location_repository.query_by_name_and_id_or_create(location_name, location_id, **kwargs)

def create_measurement(measurement_name, measurement_id, **kwargs):
    return measurement_repository.query_by_name_and_id_or_create(measurement_name, measurement_id, **kwargs)

def update_source(source, **kwargs):
    source_repository.update(source, **kwargs)
    
def update_location(location, **kwargs):
    location_repository.update(location, **kwargs)
    
def update_measurement(measurement, **kwargs):
    measurement_repository.update(measurement, **kwargs)
    
def delete_source(source):
    source_repository.delete(source)
    
def delete_location(location):
    location_repository.delete(location)
    
def delete_measurement(measurement):
    measurement_repository.delete(measurement)
