from ctypes import Union
import pytest
from OpenAQDataPlatform.tests.app.test_session import db_session
from OpenAQDataPlatform.app.unit_of_work.abstract_uow import UnitOfWork
from OpenAQDataPlatform.app.models.orm import Source 
from OpenAQDataPlatform.app.repostiories import SourceRepository


# Defining fixtures for testing Unit of Work

@pytest.fixture
def uow(db_session):
    source_repository = SourceRepository(db_session)
    uow = UnitOfWork(source_repository)
    yield uow
    
    db_session.rollback()

def test_commit(uow):
    source:Source = Source(
        source_name="test_source1",
        source_id="test_source1",
        source_type="test_type",
        source_url="http://test_url.com",
        source_description="test_description",
        source_contact="test_contact",
    )
    with uow:
        uow.repository_object.get_or_create(source)
    with uow:
        retrived_source = uow.repository_object.query_by_id("test_source1")
        assert retrived_source is not None
        assert retrived_source.source_name == "test_source1"