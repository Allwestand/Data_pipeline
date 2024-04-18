from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone

with DAG(
    "my_first_dag",
    start_date=timezone.datetime(2024,4,17),
    schedule=None,
    tags=["CS252"],
):
    my_first_task=EmptyOperator(task_id="my_first_task")
    my_second_task=EmptyOperator(task_id="my_second_task")

    my_first_task >> my_second_task