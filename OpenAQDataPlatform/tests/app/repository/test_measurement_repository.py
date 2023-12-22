from datetime import datetime
from OpenAQDataPlatform.tests.app.test_session import db_session
from OpenAQDataPlatform.app.models.orm import Measurement
from OpenAQDataPlatform.app.repostiories import MeasurementRepository

def test_get_or_create_measurement(db_session):
    measurement_repository = MeasurementRepository(db_session)
    # Create a new measurement
    new_measurement = measurement_repository.get_or_create(
        locations_id="test_locations_1", parameter="test_param", value=1, unit="test", date=datetime(2021, 1, 1), source_id="test_source1"
    )
    # Test that a new measurement was created
    assert new_measurement is not None
    assert db_session.query(Measurement).filter_by(locations_id="test_locations_1", parameter="test_param", date=datetime(2021, 1, 1)).count() == 1

    # Retrieve the existing measurement
    existing_measurement = measurement_repository.get_or_create(
        locations_id="test_locations_1", parameter="test_param", value=1, unit="test", date=datetime(2021, 1, 1), source_id="test_source1"
    )
    # Test that the existing measurement was retrieved, not created anew
    assert existing_measurement == new_measurement

def test_update(db_session):
    measurement_repository = MeasurementRepository(db_session)
    test_measurement = measurement_repository.get_or_create(
        locations_id="test_locations_2", parameter="test_param", value=1, unit="test", date=datetime(2021, 1, 1), source_id="test_source1"
    )
    # Update the measurement
    measurement_repository.update(test_measurement, value=2, unit="updated_test")
    
    updated_measurement = db_session.query(Measurement).filter_by(locations_id="test_locations_2", parameter="test_param", date=datetime(2021, 1, 1)).first()
    assert updated_measurement.value == 2 and updated_measurement.unit == "updated_test"


def test_query_by_locations_id(db_session):
    measurement_repository = MeasurementRepository(db_session)
    # Create a new measurement
    new_measurement = measurement_repository.get_or_create(
        locations_id="test_locations_3", parameter="test_param", value=1, unit="test", date=datetime(2021, 1, 1), source_id="test_source1"
    )
    # Test that a new measurement was created
    assert new_measurement is not None
    assert db_session.query(Measurement).filter_by(locations_id="test_locations_3", parameter="test_param", date=datetime(2021, 1, 1)).count() == 1

    # Retrieve the existing measurement
    existing_measurement = measurement_repository.query_by_locations_id("test_locations_3")
    # Test that the existing measurement was retrieved, not created anew
    assert existing_measurement == [new_measurement]
    
def test_query_by_source_id(db_session):
    measurement_repository = MeasurementRepository(db_session)
    # Create a new measurement
    new_measurement = measurement_repository.get_or_create(
        locations_id="test_locations_4", parameter="test_param", value=1, unit="test", date=datetime(2021, 1, 1), source_id="test_source3"
    )
    # Test that a new measurement was created
    assert new_measurement is not None
    assert db_session.query(Measurement).filter_by(locations_id="test_locations_4", parameter="test_param", date=datetime(2021, 1, 1)).count() == 1

    # Retrieve the existing measurement
    existing_measurement = measurement_repository.query_by_source_id("test_source3")
    # Test that the existing measurement was retrieved, not created anew
    assert existing_measurement == [new_measurement]
    
def test_query_by_parameter_id(db_session):
    measurement_repository = MeasurementRepository(db_session)
    # Create a new measurement
    new_measurement = measurement_repository.get_or_create(
        locations_id="test_locations_5", parameter="test_param_new", value=1, unit="test", date=datetime(2021, 1, 1), source_id="test_source4"
    )
    # Test that a new measurement was created
    assert new_measurement is not None
    assert db_session.query(Measurement).filter_by(locations_id="test_locations_5", parameter="test_param_new", date=datetime(2021, 1, 1)).count() == 1

    # Retrieve the existing measurement
    existing_measurement = measurement_repository.query_by_parameter("test_param_new")
    # Test that the existing measurement was retrieved, not created anew
    assert existing_measurement == [new_measurement]