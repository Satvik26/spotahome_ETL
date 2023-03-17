from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from spotahome_etl import run_spotahome_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020,11,8),
    'email': ['satvikbisht2699@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

dag = DAG(
    'spotahome_dag',
    default_args=default_args,
    description='Fetches of the houses for rent in given city'

)

run_etl = PythonOperator(
    task_id = 'complete_spotahome_etl',
    python_callable= run_spotahome_etl,
    dag = dag
)

run_etl


