from airflow import DAG
from airflow.operators.python import PythonOperator
from extract import weather_parameter
from datetime import datetime

default_args = {
    'owner': 'zoba',
    'retries': 1
}

dag = DAG(
    dag_id = "extract weather api to s3",
    description = "This is my dag for daily weather extraction to s3",
    start_date = datetime(2025,6,11),
    schedule_interval = "5 0 * 8 *", # runs daily at 12:05pm
    catchup= False,
    default_args = default_args
    )

extract_to_s3 = PythonOperator(
    task_id = "weather_api_to_s3",
    dag = dag,
    python_callable = weather_parameter
    )

extract_to_s3