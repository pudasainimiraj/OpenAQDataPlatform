import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from OpenAQDataPlatform.app.models.orm import Base  

@pytest.fixture(scope="module")
def db_session():
    # Use the Base metadata to create tables
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)  # Create all tables from Base
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    engine.dispose()
