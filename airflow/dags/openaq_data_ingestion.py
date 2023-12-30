import ast
import datetime
from math import log
import pandas as pd
import logging


from airflow import DAG
from airflow.exceptions import AirflowException
from airflow.decorators import task

from OpenAQDataPlatform.app.models.orm import Source,locations, Measurement
from api_utilities.get_openaq_country_list import country_list
from api_utilities.get_openaq_locations import get_all_locations
from api_utilities.get_openaq_measurement import get_all_measurement_by_country
from OpenAQDataPlatform.app.cqrs import commands

logger = logging.getLogger(__name__)
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
    def get_locations_data_into_df():
        all_locations_df = pd.DataFrame()
        list_of_countries = country_list()
        
        for country in list_of_countries:
            locations_df = get_all_locations(country[0])
            all_locations_df = pd.concat([all_locations_df, locations_df])
        
        all_locations_df.to_csv("./all_locations.csv")

    @task(task_id="get_measurement_data")
    def get_measurement_data_into_df():
        list_of_countries = country_list()
        all_measurement_df = pd.DataFrame()
        
        for country in list_of_countries:
            measurement_df = get_all_measurement_by_country(country[0])
            all_measurement_df = pd.concat([all_measurement_df, measurement_df])
        
        all_measurement_df.to_csv("./all_measurement.csv")

    @task(task_id="transform_locations" )
    def transform_locations_data():
        location_df= pd.read_csv("./all_locations.csv")
        locations_df = location_df[["id","name", "city", "country", "coordinates","manufacturers"]]
        location_df["latitude"] =  [coordinates.get('latitude',{}) if isinstance(coordinates,dict) else None for coordinates in locations_df["coordinates"]]
        location_df["longitude"] = [coordinates.get('longitude',{}) if isinstance(coordinates,dict) else None for coordinates in locations_df["coordinates"]]
        locations_df = locations_df.rename(columns={"id":"locations_id","name":"locations_name",})
        locations_df = locations_df.drop_duplicates(subset=["locations_id",])
        locations_df.to_csv("./all_locations_transform.csv")

    @task(task_id="transform_measurement")
    def transform_measurement_data():
        measurement_df = pd.read_csv("all_measurement.csv")
        logger.info(f"columns in measurement - {measurement_df.columns}")
        measurement_df = measurement_df[["locationId", "parameter", "date", "value", "unit"]]
        measurement_df = measurement_df.rename(columns={"locationId":"locations_id"})
        
        measurement_df=measurement_df.to_csv("./all_measurement_transform.csv")

    @task(task_id="load_locations", trigger_rule="none_failed")
    def load_locations():
        
        locations_df:pd.DataFrame = pd.read_csv("./all_locations_transform.csv")
        locations_df.drop(columns=["Unnamed: 0", "coordinates"], inplace=True)
        locations_df.loc[:,'locations_id'] = locations_df['locations_id'].astype(str)
        locations_df=locations_df.to_dict(orient="records")
        # locations_df["locations_id"].astype(str)
        locations_df = [locations(**location) for location in locations_df]
        try:
            commands.bulk_create_locations(locations_df)
            return "Success"
        except Exception as e:
            raise AirflowException(e)

    @task(task_id="load_measurement", trigger_rule="none_failed")
    def load_measurement( source_id:str)->str:
        measurement_df = pd.read_csv("./all_measurement_transform.csv")
        measurement_df["source_id"] = source_id
        # drop unnamed column and index column
        measurement_df.loc[:,"locations_id"]=measurement_df["locations_id"].astype(str)
        measurement_df["date"]=measurement_df['date'].apply(lambda x: ast.literal_eval(x)['utc'] if x else None)
        measurement_df.drop(columns=["Unnamed: 0"], inplace=True)
        measurement_df = measurement_df.to_dict(orient="records")
        measurement_df = [Measurement(**measurement) for measurement in measurement_df]
        try:
                commands.bulk_create_measurement(measurement_df)
                return "Success"
        except Exception as e:
            raise AirflowException(e)

    @task(task_id="load_source")
    def load_source()->str:
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
            commands.create_source(source)
            return source.source_id
        except Exception as e:
            raise AirflowException(e)
 


    locations_df_task = get_locations_data_into_df()
    measurement_df_task = get_measurement_data_into_df()
    
    location_transformation_task = transform_locations_data()
    measurement_transfomation_task = transform_measurement_data()

    # Pass task outputs as parameters to subsequent tasks
    load_locations_task = load_locations()
    load_measurement_task = load_measurement(load_source())

    # Set up task dependencies
    measurement_df_task >>measurement_transfomation_task>> load_measurement_task
    locations_df_task >>location_transformation_task
        