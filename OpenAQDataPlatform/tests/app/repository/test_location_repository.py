from cgi import test
from OpenAQDataPlatform.migrations import locations
from OpenAQDataPlatform.tests.app.test_session import db_session
from OpenAQDataPlatform.app.models.orm import locations
from OpenAQDataPlatform.app.repostiories.locations_repository import locationsRepository

def test_get_or_create_locations(db_session):
    locations_repository = locationsRepository(db_session)
    # Create a new locations
    new_locations = locations_repository.get_or_create(
        model=locations(
            locations_id="test_locations1",
            locations_name="test_locations1",
            country="test_country",
            city="test_city",
            latitude=1.0,
            longitude=1.0,
            count=1,
        )
    )
    # Test that a new locations was created
    assert new_locations is not None
    assert (
        db_session.query(locations)
        .filter_by(
            locations_id="test_locations1",
            locations_name="test_locations1",
            country="test_country",
            city="test_city",
            latitude=1.0,
            longitude=1.0,
            count=1,
        )
        .count()
        == 1
    )

    # Retrieve the existing locations
    existing_locations = locations_repository.get_or_create(
        model=locations(
            locations_id="test_locations1",
            locations_name="test_locations1",
            country="test_country",
            city="test_city",
            latitude=1.0,
            longitude=1.0,
            count=1,
        )
    )
    # Test that the existing locations was retrieved, not created anew
    assert existing_locations == new_locations
    
def test_update_locations(db_session):
    locations_repository = locationsRepository(db_session)
    test_locations = locations_repository.get_or_create(
        model=locations(
            locations_id="test_locations2",
            locations_name="test_locations2",
            country="test_country",
            city="test_city",
            latitude=1.0,
            longitude=1.0,
            count=1,
        )
    )
    # Update the locations
    locations_repository.update(test_locations, city="updated_city", country="updated_country")
    
    updated_locations = db_session.query(locations).filter_by(locations_id="test_locations2").first()
    assert updated_locations.city == "updated_city" and updated_locations.country == "updated_country"
    
def test_query_by_id(db_session):
    locations_repository = locationsRepository(db_session)
    test_locations = locations_repository.get_or_create(
        model=locations(
            locations_id="test_locations1",
            locations_name="test_locations1",
            country="test_country",
            city="test_city",
            latitude=1.0,
            longitude=1.0,
            count=1,
        )
    )
    # Query the locations
    locations_query = locations_repository.query_by_id("test_locations1")
    
    assert locations_query == test_locations

def test_query_all(db_session):
    locations_repository = locationsRepository(db_session)
    # Query all locationss
    locations_query = locations_repository.query_all()
    assert locations_query is not None
