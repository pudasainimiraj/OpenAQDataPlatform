
from enum import unique
from sqlalchemy import Boolean, Float, MetaData, Column, String, ForeignKey, DateTime, Integer
from sqlalchemy.orm import declarative_base, relationship



Base = declarative_base()
metadata = MetaData()

class locations(Base):
    __tablename__ = 'locations'
    locations_id = Column(String, primary_key=True, unique=True)
    locations_name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    manufacturers = Column(String)
    count = Column(Integer)

    measurements = relationship('Measurement', back_populates='locations')

class Measurement(Base):
    __tablename__ = 'measurement'
    locations_id = Column(String, ForeignKey('locations.locations_id'), primary_key=True)
    parameter = Column(String, primary_key=True)  # Part of the composite primary key
    date = Column(DateTime, primary_key=True)  # Part of the composite primary key
    value = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    average = Column(Float)
    source_id = Column(String, ForeignKey('source.source_id'))
    
  
    # Relationships
    locations = relationship('locations', back_populates='measurements')
    source = relationship('Source', back_populates='measurements')

class Source(Base):
    __tablename__ = 'source'
    source_name = Column(String, primary_key=True)
    source_url = Column(String, nullable=False)
    source_type = Column(String, nullable=False)
    source_id = Column(String, nullable=False, unique=True)
    source_description = Column(String)
    source_contact = Column(String)
    source_active = Column(Boolean)
    measurements = relationship('Measurement', back_populates='source')
