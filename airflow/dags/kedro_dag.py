from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

PROJECT_PATH = "/opt/airflow/project"

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 10, 21),
    "retries": 1,
    "retry_delay": timedelta(minutes=3),
}

with DAG(
    dag_id="kedro_project_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=["kedro", "mlops"],
) as dag:

    eda = BashOperator(
        task_id="eda_pipeline",
        bash_command=f"""
        set -e
        cd {PROJECT_PATH}
        python3 -m kedro run --pipeline=eda
        """
    )

    preprocessing = BashOperator(
        task_id="preprocessing_pipeline",
        bash_command=f"""
        set -e
        cd {PROJECT_PATH}
        python3 -m kedro run --pipeline=preprocessing
        """
    )

    modeling = BashOperator(
        task_id="modeling_pipeline",
        bash_command=f"""
        set -e
        cd {PROJECT_PATH}
        python3 -m kedro run --pipeline=modeling
        """
    )

    eda >> preprocessing >> modeling
