# from datetime import datetime
# import pytest
# from OpenAQDataPlatform.tests.app.unit_of_work.test_abstract_uow import uow
# from OpenAQDataPlatform.tests.app.test_session import db_session
# from OpenAQDataPlatform.app.models.orm import locations, Source, Measurement
# from OpenAQDataPlatform.app.unit_of_work.abstract_uow import UnitOfWork
# from OpenAQDataPlatform.app.repostiories import (
#     SourceRepository,
# )
# from OpenAQDataPlatform.app.cqrs.commands import (
#     create_locations,
#     create_source,
#     create_measurement,
#     delete_measurement,
#     update_locations,
#     update_source,
#     update_measurement,
#     delete_locations,
#     delete_source,
#     delete_measurement,
# )
# from OpenAQDataPlatform.app.repostiories import (
#     source_repository,
#     locations_repository,
#     measurement_repository,
# )


# def test_create_source(uow):
#     source:Source = Source(
#         source_name="test_source1",
#         source_id="test_source1",
#         source_type="test_type",
#         source_url="http://test_url.com",
#         source_description="test_description",
#         source_contact="test_contact",
#     )
#     with uow:
#         source_created=uow.repository_object.get_or_create(source)
#         assert source_created is not None
#         assert source_created.source_name == "test_source1"
