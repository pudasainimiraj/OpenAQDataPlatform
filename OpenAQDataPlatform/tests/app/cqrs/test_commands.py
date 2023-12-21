# from datetime import datetime

# from numpy import source
# from OpenAQDataPlatform.tests.app.test_session import db_session
# from OpenAQDataPlatform.app.models.orm import Location, Source, Measurement
# from OpenAQDataPlatform.app.cqrs.commands import (
#     create_location,
#     create_source,
#     create_measurement,
#     delete_measurement,
#     update_location,
#     update_source,
#     update_measurement,
#     delete_location,
#     delete_source,
#     delete_measurement,
# )
# from OpenAQDataPlatform.app.repostiories import (
#     source_repository,
#     location_repository,
#     measurement_repository,
# )
# def test_create_source(db_session):
#     # Create a new source
#     created_source = create_source(db_session, model=Source(
#         source_name="test_source1",
#         source_id="test_source1",
#         source_type="test_type",
#         source_url="http://test_url.com",
#         source_description="test_description",
#         source_contact="test_contact",
#     ))
    
#     assert created_source is not None
#     assert created_source.source_name == "test_source1"
#     assert created_source.source_id == "test_source1"

# # Update the source created in the previous test
# def test_update_source(db_session):
#     source_to_update = source_repository.query_by_id(db_session, "test_source1")
#     updated_source = update_source(
#         source_to_update,
#         source_name="test_source2",
#         source_id="test_source2",
#         source_type="test_type",
#         source_url="http://test_url.com",
#         source_description="test_description",
#         source_contact="test_contact",
#     )
    
#     assert updated_source is not None
#     assert updated_source.source_name == "test_source2"
#     assert updated_source.source_id == "test_source2"

# # Delete the source created in the previous test
# def test_delete_source(db_session):
#     source_to_delete = source_repository.query_by_id(db_session, "test_source2")
#     delete_source(source_to_delete)
    
#     assert source_repository.query_by_id(db_session, "test_source2") is None

# # Modify other test cases similarly by passing db_session to repository methods


# def test_create_location(db_session):
#     # Create a new location
#     location:Location=create_location(Location(
#         location_id="test_location1",
#         location_name="test_location1",
#         country="test_country",
#         city="test_city",
#         latitude=1.0,
#         longitude=1.0,
#         count=1,
#     ))
    
#     assert location is not None
#     assert location.location_id == "test_location1"
#     assert location.location_name == "test_location1"

# def test_update_location(db_session):
#     # Update the location created in the previous test
#     updated_location:Location=update_location(
#         location_repository.query_by_id("test_location1"),
#         location_id="test_location2",
#         location_name="test_location2",
#         country="test_country",
#         city="test_city",
#         latitude=1.0,
#         longitude=1.0,
#         count=1,
#     )
    
#     assert updated_location is not None
#     assert updated_location.location_id == "test_location2"
#     assert updated_location.location_name == "test_location2"

# def test_delete_location(db_session):
#     # Delete the location created in the previous test
#     delete_location(location_repository.query_by_id("test_location2"))
    
#     assert location_repository.query_by_id("test_location2") is None
    
# def test_create_measurement(db_session):
#     # Create a new measurement
#     measurement:Measurement=create_measurement(Measurement(
#         location_id="test_location1",
#         parameter="test_param",
#         date=datetime(2021, 1, 1),
#         value=1,
#         unit="test",
#         source_id="test_source1",
#     ))
    
#     assert measurement is not None
#     assert measurement.location_id == "test_location1"
#     assert measurement.parameter == "test_param"

# def test_update_measurement(db_session):
#     # Update the measurement created in the previous test
#     updated_measurement:Measurement=update_measurement(
#         measurement_repository.query_by_id("test_location1", "test_param", datetime(2021, 1, 1)),
#         location_id="test_location2",
#         parameter="test_param",
#         date=datetime(2021, 1, 1),
#         value=1,
#         unit="test",
#         source_id="test_source1",
#     )
    
#     assert updated_measurement is not None
#     assert updated_measurement.location_id == "test_location2"
#     assert updated_measurement.parameter == "test_param"

# def test_delete_measurement(db_session):
#     # Delete the measurement created in the previous test
#     delete_measurement(measurement_repository.query_by_id("test_location2", "test_param", datetime(2021, 1, 1)))
    
#     assert measurement_repository.query_by_id("test_location2", "test_param", datetime(2021, 1, 1)) is None
