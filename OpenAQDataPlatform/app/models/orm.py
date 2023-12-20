import re
from sqlalchemy import (
    Boolean,
    Float,
    Index,
    Table,
    MetaData,
    Column,
    String,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import relationship, registry
from models import Location, Measurement, Source

mapper_registry = registry()
metadata = MetaData()

location = Table(
    "location",
    metadata,
    Column("location_id", String, primary_key=True),
    Column("location_name", String, nullable=False),
    Column("city", String),
    Column("country", String, nullable=False),
    Column("latitude", Float),
    Column("longitude", Float),
)

measurement = Table(
    "measurement",
    metadata,
    Column("location_id", String, ForeignKey("location.location_id")),
    Column("parameter", String, nullable=False),
    Column("value", Float, nullable=False),
    Column("unit", String, nullable=False),
    Column("date", DateTime, nullable=False),
    Column("source_name", String, ForeignKey("source.source_name")),
)

source = Table(
    "source",
    Column("source_name", String, primary_key=True),
    Column("source_url", String, nullable=False),
    Column("source_type", String, nullable=False),
    Column("source_id", String, nullable=False),
    Column("source_description", String),
    Column("source_contact", String),
    Column("source_active", Boolean),
)

Index("ix_measurement_location_id_date", measurement.c.location_id, measurement.c.date)
mapper_registry.map_imperatively(
    Measurement, 
    measurement, 
    properties={
        "location": relationship(Location, backref="measurement"),
        "source": relationship(Source, backref="measurement")
    }
)

