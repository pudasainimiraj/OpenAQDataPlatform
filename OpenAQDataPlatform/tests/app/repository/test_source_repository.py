from OpenAQDataPlatform.app.models.orm import Source
from OpenAQDataPlatform.tests.app.test_session import db_session
from OpenAQDataPlatform.app.repostiories.source_repository import SourceRepository

def test_get_or_create_source(db_session):
    source_repository = SourceRepository(db_session)
    # Create a new source
    new_source = source_repository.get_or_create_source(
        model=Source(
            source_name="test_source1",
            source_url="https://example.com",
            source_type="test",
            source_id="test_source1",
            source_description="Test source",
            source_contact="test@example.com",
            source_active=True,
        )
    )
    # Test that a new source was created
    assert new_source is not None
    assert (
        db_session.query(Source)
        .filter_by(
            source_name="test_source1",
            source_url="https://example.com",
            source_type="test",
            source_id="test_source1",
            source_description="Test source",
            source_contact="test@example.com",
            source_active=True,
        )
        .count()
        == 1
    )

    # Retrieve the existing source
    existing_source = source_repository.get_or_create_source(
        model=Source(
            source_name="test_source1",
            source_url="https://example.com",
            source_type="test",
            source_id="test_source1",
            source_description="Test source",
            source_contact="test@example.com",
            source_active=True,
        )
    )
    # Test that the existing source was retrieved, not created anew
    assert existing_source == new_source

def test_update(db_session):
    source_repository = SourceRepository(db_session)
    test_source = source_repository.get_or_create_source(
        model=Source(
            source_name="test_source2",
            source_url="https://example.com",
            source_type="test",
            source_id="test_source2",
            source_description="Test source",
            source_contact="test@example.com",
            source_active=True,
        )
    )
    # Update the source
    source_repository.update(test_source, source_name="updated_test_source")
    
    updated_source = db_session.query(Source).filter_by(source_id="test_source2").first()
    assert updated_source.source_name == "updated_test_source"
    
def test_query_by_id(db_session):
    source_repository = SourceRepository(db_session)
    # Create a new source
    new_source = source_repository.get_or_create_source(
        model=Source(
            source_name="test_source3",
            source_url="https://example.com",
            source_type="test",
            source_id="test_source3",
            source_description="Test source",
            source_contact="test@example.com",
            source_active=True,
        )
    )
    # Test that a new source was created
    assert new_source is not None
    assert (
        db_session.query(Source)
        .filter_by(
            source_name="test_source3",
            source_url="https://example.com",
            source_type="test",
            source_id="test_source3",
            source_description="Test source",
            source_contact="test@example.com",
            source_active=True,
        )
        .count()
        == 1
    )

    # Retrieve the existing source
    existing_source = source_repository.query_by_id("test_source3")
    # Test that the existing source was retrieved, not created anew
    assert existing_source == new_source

def test_query_all(db_session):
    source_repository = SourceRepository(db_session)
    # Create a new source
    new_source = source_repository.get_or_create_source(
        model=Source(
            source_name="test_source4",
            source_url="https://example.com",
            source_type="test",
            source_id="test_source4",
            source_description="Test source",
            source_contact="test@example.com",
            source_active=True,
        )
    )
    # Test that a new source was created
    assert new_source is not None
    assert (
        db_session.query(Source)
        .filter_by(
            source_name="test_source4",
            source_url="https://example.com",
            source_type="test",
            source_id="test_source4",
            source_description="Test source",
            source_contact="test@example.com",
            source_active=True,
        )
        .count()
        == 1
    )

    # Retrieve the existing source
    existing_source = source_repository.query_all()
    # Test that the existing source was retrieved, not created anew
    assert len(existing_source) == 4

