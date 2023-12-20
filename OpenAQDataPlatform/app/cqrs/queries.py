from OpenAQDataPlatform.app.repostiories import source_repository, location_repository, measurement_repository

def get_all_measurements():
    return measurement_repository.query_all()

def get_all_sources():
    return source_repository.query_all()

def get_all_locations():
    return location_repository.query_all()

def get_all_measurements_by_source(source):
    source_id=source.source_id
    return measurement_repository.query_by_source_id(source_id)

def get_all_measurements_by_location(location):
    location_id=location.location_id
    return measurement_repository.query_by_location_id(location_id)

def filter_measurements_by_date( start_date, end_date):
    return measurement_repository.query_by_date( start_date, end_date)

def filter_measurements_by_value( value):
    return measurement_repository.query_by_value( value)

def filter_measurements_by_parameter( parameter):
    return measurement_repository.query_by_parameter( parameter)
