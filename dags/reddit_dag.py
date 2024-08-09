from airflow import DAG
from datetime import datetime
import os
import sys

from airflow.operators.python import PythonOperator


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline

# dag_directory = os.path.dirname(os.path.abspath(__file__))
# project_directory = os.path.dirname(dag_directory)
# sys.path.insert(0, project_directory)

default_args = {
    'owner': 'Varun MJ',
    'start_date': datetime(2024, 8, 7),
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)