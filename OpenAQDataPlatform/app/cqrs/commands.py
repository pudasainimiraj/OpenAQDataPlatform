from OpenAQDataPlatform.app.unit_of_work import UnitOfWork
from OpenAQDataPlatform.app.repostiories import source_repository, locations_repository, measurement_repository
from OpenAQDataPlatform.app.models.orm import Source, locations, Measurement

def bulk_create_locations(model_list:list)->None:
    try:
        with UnitOfWork(locations_repository) as uow:
             uow.repository_object.get_or_create_batch(model_list)
             uow.commit()
    except Exception as e:
        raise e
        
def bulk_create_measurement(model_list:list)->None:
    try:
        with UnitOfWork(measurement_repository) as uow:
            uow.repository_object.get_or_create_batch(model_list)
            uow.commit()
    except Exception as e:
        raise e
    
def create_source(model:Source)-> dict:
    try:
        with UnitOfWork(source_repository) as uow:
            source = uow.repository_object.get_or_create(model)
            uow.commit()
            return source
    except Exception as e:
        raise e

def create_locations(model:locations)->locations:
    try:
        with UnitOfWork(locations_repository) as uow:
            return uow.repository_object.get_or_create(model)
    except Exception as e:
        raise e

def create_measurement(model:Measurement)->Measurement:
    
    try:
        with UnitOfWork(measurement_repository) as uow:
            return uow.repository_object.get_or_create(model)
    except Exception as e:
        raise e
    

def update_source(model:Source, **kwargs)->Source:
    try:
        with UnitOfWork(source_repository) as uow:
            uow.repository_object.update(model, **kwargs)
    except Exception as e:
        raise e

def update_locations(model:locations, **kwargs)->locations:
    try:
        with UnitOfWork(locations_repository) as uow:
            uow.repository_object.update(model, **kwargs)
    except Exception as e:
        raise e
    
def update_measurement(model:Measurement, **kwargs)->Measurement:
    try:
        with UnitOfWork(measurement_repository) as uow:
            uow.repository_object.update(model, **kwargs)
    except Exception as e:
        raise e
    
def delete_source(model:Source)->Source:
    try:
        with UnitOfWork(source_repository) as uow:   
            uow.repository_object.delete(model)
    except Exception as e:
        raise e
    
def delete_locations(model:locations)->locations:
    try:
        with UnitOfWork(locations_repository) as uow:
            uow.repository_object.delete(model)
    except Exception as e:
        raise e
    
def delete_measurement(model:Measurement)->Measurement:
    try:
        with UnitOfWork(measurement_repository) as uow:
            uow.repository_object.delete(model)
    except Exception as e:
        raise e