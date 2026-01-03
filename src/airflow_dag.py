from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def run_pipeline():
    print("Pipeline executed")

with DAG(
    "loan_approval_time_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@weekly",
    catchup=False,
) as dag:
    run = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_pipeline
    )
