from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from spread import mates_name



default_args ={
    'owner': 'Eze_cynthia',
    'retries': 3,
    'retry_delay': timedelta(seconds=10)


}

run_dag=DAG(
    dag_id="chizoba_gspread",
    description="google sheet data uploaded",
    default_args=default_args
)


task_one=PythonOperator(
    dag=run_dag,
    python_callable=mates_name,
    task_id= "task_one"
)

task_one

