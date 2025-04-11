from datetime import datetime as dt
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'etl_user',
    'depends_on_past': False,
    'start_date': dt(2025, 4, 8),
}

dag = DAG('DAG_1', default_args=default_args, schedule_interval='0 1 * * *', catchup=True,
          max_active_tasks=1, max_active_runs=1, tags=['Lab4'])

tsk1 = BashOperator(
    task_id='task1',
    bash_command='python3 /home/balots/airflow/scripts/DAG_1/task1.py',
    dag=dag
)

tsk2 = BashOperator(
    task_id='task2',
    bash_command='python3 /home/balots/airflow/scripts/DAG_1/task2.py',
    dag=dag
)