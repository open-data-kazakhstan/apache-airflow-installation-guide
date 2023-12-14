from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

# Definition of DAG parameters
default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Creating DAG object
dag = DAG(
    'my_dag_id',
    default_args=default_args,
    description='My DAG description',
    schedule_interval=timedelta(days=1),  # Execution schedule
)

# Definition of operators (tasks) in DAG
start_task = DummyOperator(task_id='start_task', dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

# Definition of task execution order
start_task >> end_task
