from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    "hello",
    default_args={
        "depends_on_past": False,
        "retries": 1,
         "retry_delay": timedelta(minutes=1),
    },
    description="Prints hello",
    schedule=timedelta(days=1),
    start_date=datetime(2026,11,10),
    catchup=False,
    tags=["hello"]
) as dag:
    t1 = BashOperator(
        task_id="print_hello",
        bash_command="echo hello",
    )

    t2 = BashOperator(
        task_id="sleep",
        bash_command="sleep 5",
        retries=3,
    )

    t1 >> t2