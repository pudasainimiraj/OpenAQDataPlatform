from OpenAQDataPlatform.app.models.orm import Source, Location, Measurement
from OpenAQDataPlatform.app.unit_of_work.abstract_uow import UnitOfWork
from OpenAQDataPlatform.app.repostiories import (
    SourceRepository,
    LocationRepository,
    MeasurementRepository,
)


def create_source(model:Source):
    with UnitOfWork(SourceRepository) as uow:
        source = uow.repository_object.get_or_create(model)
        uow.commit()
        return source

def create_location(model:Location):
    with UnitOfWork(LocationRepository) as uow:
        location = uow.repository_object.get_or_create(model)
        uow.commit()
        return location

def create_measurement(model:Measurement):
    with UnitOfWork(MeasurementRepository) as uow:
        measurement = uow.repository_object.get_or_create(model)
        uow.commit()
        return measurement

def update_source(model:Source, **kwargs):
    with UnitOfWork(SourceRepository) as uow:
        uow.repository_object.update(model, **kwargs)
        uow.commit()

def update_location(model:Location, **kwargs):
    with UnitOfWork(LocationRepository) as uow:
        uow.repository_object.update(model, **kwargs)
        uow.commit()

def update_measurement(model:Measurement, **kwargs):
    with UnitOfWork(MeasurementRepository) as uow:
        uow.repository_object.update(model, **kwargs)
        uow.commit()

def delete_source(model:Source):
    with UnitOfWork(SourceRepository) as uow:
        uow.repository_object.delete(model)
        uow.commit()

def delete_location(model:Location):
    with UnitOfWork(LocationRepository) as uow:
        uow.repository_object.delete(model)
        uow.commit()

def delete_measurement(model:Measurement):
    with UnitOfWork(MeasurementRepository) as uow:
        uow.repository_object.delete(model)
        uow.commit()