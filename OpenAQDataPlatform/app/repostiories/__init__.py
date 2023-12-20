# Desc: This file is used to import all the repositories in the app

from .location_repository import LocationRepository
from .measurement_repository import MeasurementRepository
from .source_repository import SourceRepository
from .base_repository import BaseRepository

base_repository = BaseRepository
source_repository = SourceRepository
location_repository = LocationRepository
measurement_repository = MeasurementRepository