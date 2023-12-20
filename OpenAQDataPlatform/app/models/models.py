from dataclasses import dataclass
from typing import Union
from datetime import datetime

@dataclass
class BaseDataClass:
    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if value is None:
                raise ValueError(f"Missing value for {field.name}")
    
    def __str__(self):
        return str(self.__dict__)
    

@dataclass
class Location(BaseDataClass):
    location_id: str
    location_name: str
    city: Union[str, None] = None
    country: str
    latitude: Union[float, None] = None
    longitude: Union[float, None] = None

@dataclass
class Measurement(BaseDataClass):
    location_id: str
    parameter: str
    value: float
    unit: str
    date: datetime.datetime
    latitude: Union[float, None] = None
    longitude: Union[float, None] = None

@dataclass
class Source(BaseDataClass):
    source_name: str
    source_url: str
    source_type: str
    source_id: str
    source_description: Union[str, None] = None
    source_contact: Union[str, None] = None
    source_active: Union[bool, None] = None
