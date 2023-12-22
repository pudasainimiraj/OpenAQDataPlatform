# Desc: This file is used to import all the repositories in the app

from .locations_repository import locationsRepository
from .measurement_repository import MeasurementRepository
from .source_repository import SourceRepository
from .base_repository import BaseRepository

base_repository:BaseRepository = BaseRepository
source_repository:SourceRepository = SourceRepository
locations_repository:locationsRepository = locationsRepository
measurement_repository:MeasurementRepository = MeasurementRepository