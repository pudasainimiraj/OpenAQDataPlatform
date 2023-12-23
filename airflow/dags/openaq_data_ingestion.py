import datetime
from json import load
from numpy import source
import pandas as pd
from OpenAQDataPlatform.app.models.orm import Source


from airflow import DAG
from airflow.exceptions import AirflowException
from airflow.decorators import task

from api_utilities.get_openaq_country_list import country_list
from api_utilities.get_openaq_locations import get_all_locations
from api_utilities.get_openaq_measurement import get_all_measurement_by_country
from OpenAQDataPlatform.app.unit_of_work import UnitOfWork


default_args = {
    "owner": "airflow",
    "start_date": datetime.datetime(2021, 1, 1),
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=5),
}

dag = DAG(
    'simple_openaq_ingestion',
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["openaq"],
)


with dag:
    @task(task_id="get_locations_data")
    def get_locations_data_into_df()->pd.DataFrame:
        all_locations_df = pd.DataFrame()
        list_of_countries = country_list()
        
        for country in list_of_countries:
            locations_df = get_all_locations(country[0])
            all_locations_df = pd.concat([all_locations_df, locations_df])
        
        return all_locations_df

    @task(task_id="get_measurement_data")
    def get_measurement_data_into_df()->pd.DataFrame:
        list_of_countries = country_list()
        all_measurement_df = pd.DataFrame()
        
        for country in list_of_countries:
            measurement_df = get_all_measurement_by_country(country[0])
            all_measurement_df = pd.concat([all_measurement_df, measurement_df])
        
        return all_measurement_df

    @task(task_id="transform_locations", )
    def transform_locations_data(locations_df:pd.DataFrame)->pd.DataFrame:
        locations_df = locations_df[["id","name", "city", "country", "coordinates","sources","manufacturers","count"]]
        locations_df["longitude"] = locations_df["coordinates"].apply(lambda x: x["longitude"])
        locations_df["latitude"] = locations_df["coordinates"].apply(lambda x: x["latitude"])
        locations_df = locations_df.rename(columns={"id":"locations_id","name":"locations_name",})
        locations_df = locations_df.drop_duplicates(subset=["locations_id",])
        return locations_df

    @task(task_id="transform_measurement")
    def transform_measurement_data(measurement_df:pd.DataFrame)->pd.DataFrame:
        measurement_df = measurement_df[["locationsId", "parameter", "date", "value", "unit"]]
        measurement_df = measurement_df.rename(columns={"locations":"locations_id"})
    
        return measurement_df

    @task(task_id="load_locations")
    def load_locations(locations_df: pd.DataFrame)->str:
        locations_repository = locations_repository
        locations_df = transform_locations_data(locations_df)
        locations_df = locations_df.to_dict(orient="records")
        locations_df = [Source(**location) for location in locations_df]
        try:
            with UnitOfWork(locations_repository) as uow:
                uow.repository_object.get_or_create_batch(locations_df)
                return "Success"
        except Exception as e:
            raise AirflowException(e)

    @task(task_id="load_measurement")
    def load_measurement(measurement_df: pd.DataFrame, source_id)->str:
        measurement_repository = measurement_repository
        measurement_df = transform_measurement_data(measurement_df)
        measurement_df["source_id"] = source_id
        measurement_df = measurement_df.to_dict(orient="records")
        measurement_df = [Source(**measurement) for measurement in measurement_df]
        try:
            with UnitOfWork(measurement_repository) as uow:
                uow.repository_object.get_or_create_batch(measurement_df)
                return "Success"
        except Exception as e:
            raise AirflowException(e)

    @task(task_id="load_source")
    def load_source()->str:
        source_repository = source_repository
        source = Source(
            source_name="OpenAQ",
            source_url="https://docs.openaq.org/",
            source_type="Open Source",
            source_id="openaq",
            source_description="OpenAQ is a community of scientists, software developers, and lovers of open environmental data.",
            source_contact="https://docs.openaq.org/",
            source_active=True
        )
        try:
            with UnitOfWork(source_repository) as uow:
                uow.repository_object.get_or_create(source)
            return source
        except Exception as e:
            raise AirflowException(e)
 
    source_task = load_source()
    locations_df_task = get_locations_data_into_df()
    measurement_df_task = get_measurement_data_into_df()
    
    
    load_locations_task = load_locations(locations_df_task)
    load_measurement_task = load_measurement(measurement_df_task, source_task)
    
    source_task >> load_locations_task >> load_measurement_task
    
        