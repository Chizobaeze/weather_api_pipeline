FROM apache/airflow:2.8.0

WORKDIR /gspread.com

COPY requirements.txt /gspread.com

RUN pip install --no-cache-dir -r /gspread.com/requirements.txt