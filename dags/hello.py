from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone

import logging

def _say_hello():
    logging.debug("This is Bug")
    logging.info("hello")

with DAG(
    "hello",
    start_date=timezone.datetime(2024,4,17),
    schedule=None,
    tags=["CS252"],
):
    start=EmptyOperator(task_id="start")
    echo_hello = BashOperator(
        task_id="echo_hello",
        bash_command="echo 'hello'",
    )
    say_hello=PythonOperator(
        task_id="say_hello",
        python_callable=_say_hello,
              
    
    
    )
    end=EmptyOperator(task_id="end")

    start >> echo_hello >> end