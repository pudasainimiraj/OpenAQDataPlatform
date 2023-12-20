from cgi import test
from OpenAQDataPlatform.migrations import location
from OpenAQDataPlatform.tests.app.test_session import db_session
from OpenAQDataPlatform.app.models.orm import Location
from OpenAQDataPlatform.app.repostiories.location_repository import LocationRepository

def test_get_or_create_location(db_session):
    location_repository = LocationRepository(db_session)
    # Create a new location
    new_location = location_repository.get_or_create_location(
        model=Location(
            location_id="test_location1",
            location_name="test_location1",
            country="test_country",
            city="test_city",
            latitude=1.0,
            longitude=1.0,
            count=1,
        )
    )
    # Test that a new location was created
    assert new_location is not None
    assert (
        db_session.query(Location)
        .filter_by(
            location_id="test_location1",
            location_name="test_location1",
            country="test_country",
            city="test_city",
            latitude=1.0,
            longitude=1.0,
            count=1,
        )
        .count()
        == 1
    )

    # Retrieve the existing location
    existing_location = location_repository.get_or_create_location(
        model=Location(
            location_id="test_location1",
            location_name="test_location1",
            country="test_country",
            city="test_city",
            latitude=1.0,
            longitude=1.0,
            count=1,
        )
    )
    # Test that the existing location was retrieved, not created anew
    assert existing_location == new_location
    
def test_update_location(db_session):
    location_repository = LocationRepository(db_session)
    test_location = location_repository.get_or_create_location(
        model=Location(
            location_id="test_location2",
            location_name="test_location2",
            country="test_country",
            city="test_city",
            latitude=1.0,
            longitude=1.0,
            count=1,
        )
    )
    # Update the location
    location_repository.update(test_location, city="updated_city", country="updated_country")
    
    updated_location = db_session.query(Location).filter_by(location_id="test_location2").first()
    assert updated_location.city == "updated_city" and updated_location.country == "updated_country"
    
def test_query_by_id(db_session):
    location_repository = LocationRepository(db_session)
    test_location = location_repository.get_or_create_location(
        model=Location(
            location_id="test_location1",
            location_name="test_location1",
            country="test_country",
            city="test_city",
            latitude=1.0,
            longitude=1.0,
            count=1,
        )
    )
    # Query the location
    location_query = location_repository.query_by_id("test_location1")
    
    assert location_query == test_location

def test_query_all(db_session):
    location_repository = LocationRepository(db_session)
    # Query all locations
    location_query = location_repository.query_all()
    assert location_query is not None
