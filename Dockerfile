FROM apache/airflow:2.8.0

WORKDIR /weather-api

COPY requirements.txt /weather-api

RUN pip install --no-cache-dir -r /weather-api/requirements.txt
