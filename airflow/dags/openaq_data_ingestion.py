import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


from utilities.get_country_list import country_list

@dag(start_date=datetime.datetime(2021, 1, 1), schedule="@daily")
def generate_dag():
    EmptyOperator(task_id="task")


generate_dag()