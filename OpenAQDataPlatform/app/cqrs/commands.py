from OpenAQDataPlatform.app.repostiories import source_repository, locations_repository, measurement_repository
from OpenAQDataPlatform.app.models.orm import Source, locations, Measurement

def bulk_create_locations(model_list:list[locations])->list[locations]:
    try:
        return locations_repository.get_or_create_batch(model_list)
    except Exception as e:
        raise e
        
def bulk_create_measurement(model_list:list[Measurement])->list[Measurement]:
    try:
        return measurement_repository.get_or_create_batch(model_list)
    except Exception as e:
        raise e
    
def create_source(model:Source)-> Source:
    try:
        return source_repository.get_or_create(model)
    except Exception as e:
        raise e

def create_locations(model:locations)->locations:
    try:
        return locations_repository.get_or_create(model)
    except Exception as e:
        raise e

def create_measurement(model:Measurement)->Measurement:
    
    try:
        return measurement_repository.get_or_create(model)
    except Exception as e:
        raise e
    

def update_source(model:Source, **kwargs)->Source:
    try:
        source_repository.update(model, **kwargs)
    except Exception as e:
        raise e

def update_locations(model:locations, **kwargs)->locations:
    try:
        locations_repository.update(model, **kwargs)
    except Exception as e:
        raise e
    
def update_measurement(model:Measurement, **kwargs)->Measurement:
    try:
        measurement_repository.update(model, **kwargs)
    except Exception as e:
        raise e
    
def delete_source(model:Source)->Source:
    try:
        source_repository.delete(model)
    except Exception as e:
        raise e
    
def delete_locations(model:locations)->locations:
    try:
        locations_repository.delete(model)
    except Exception as e:
        raise e
    
def delete_measurement(model:Measurement)->Measurement:
    try:
        measurement_repository.delete(model)
    except Exception as e:
        raise e