FROM apache/airflow:2.10.0

USER root
COPY ./airflow/sources/requirements_docker.txt /requirements_docker.txt
COPY ./data/spotify_dataset.csv /opt/airflow/data/spotify_dataset.csv
COPY ./drive_config /opt/airflow/drive_config

USER airflow
RUN pip install --no-cache-dir -r /requirements_docker.txt