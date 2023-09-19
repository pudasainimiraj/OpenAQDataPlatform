from dataclasses import dataclass
from typing import Text
from cassandra.cqlengine import columns, connection, ValidationError
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model
from uuid import uuid4
import re


"""_ORM for database_
We do not seperately do a create table kinda orm like sql alchemy cause cassandra take in the object and makes it themslef
"""


@dataclass
class Location(Model):
    location_id = columns.UUID(primary_key=True, default=uuid4)
    location= columns.Text(required=True)
    city= columns.Text(required=True)
    coutry=columns.Text(required=True)
    """this needs to change to take latitude and longitute as a combined cordinates
        or may be we could just do latitude and longitude as a different columns
        that's tbd ....
    """
    cordinates=columns.Double(required=True)

@dataclass
class Mesurement(Model):
    mesurement_id=columns.TimeUUID(primary_key=True, default=uuid4)
    date=columns.DateTime(required=True) #I think this can be optional or remove at all cause we are already using TimeUUID for mesurement ID
    location_id=columns.UUID(index=True)
    source_id=columns.UUID(index=True)
    # value is probably going to be a multiplue column as well cause there are 4distinct type of pollutant ascoiated in
    # the analysis database need to be able to handle that
    value=columns.Text(required=True)
    unit= columns.Text(required=True)
    
@dataclass
class Source(Model):
    source_id=columns.UUID(primary_key=True, default=uuid4)
    name=columns.Text(required=True)
    url=columns.Text()
    
sync_table(Location)
sync_table(Mesurement)
sync_table(Source)