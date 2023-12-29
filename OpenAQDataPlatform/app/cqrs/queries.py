import re
from OpenAQDataPlatform.app.unit_of_work import UnitOfWork
from OpenAQDataPlatform.app.repostiories import source_repository, locations_repository, measurement_repository

def get_all_measurements():
    with UnitOfWork(measurement_repository) as uow:
         uow.repository_object.query_all()

def get_all_sources():
    with UnitOfWork(source_repository) as uow:
        return uow.repository_object.query_all()

def get_all_locations():
    with UnitOfWork(locations_repository) as uow:
        return uow.repository_object.query_all()

def get_all_measurements_by_source(source):
    with UnitOfWork(measurement_repository) as uow:
        return uow.repository_object.query_by_source_id(source.source_id)

def get_all_measurements_by_locations(locations):
    locations_id=locations.locations_id
    with UnitOfWork(measurement_repository) as uow:
        return uow.repository_object.query_by_locations_id(locations_id)

def filter_measurements_by_date( start_date, end_date):
    with UnitOfWork(measurement_repository) as uow:
        return uow.repository_object.query_by_date( start_date, end_date)

def filter_measurements_by_value( value):
    with UnitOfWork(measurement_repository) as uow:
        return uow.repository_object.query_by_value( value)

def filter_measurements_by_parameter( parameter):
    with UnitOfWork(measurement_repository) as uow:
        return uow.repository_object.query_by_parameter( parameter)
