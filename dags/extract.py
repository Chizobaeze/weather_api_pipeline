import requests
import awswrangler as wr
import pandas as pd
import boto3
from airflow.models import Variable
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = Variable.get('API_KEY')
BASE_URL = "http://api.weatherbit.io/v2.0/alerts"
city_name = ['Texas']
country_name= ['US']

code_value= {
    'key':API_KEY,
    'city': city_name,
    'country': country_name
}

response = requests.get(BASE_URL, params=code_value)

def weather_parameter(response):

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame([data])

    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")

    session = boto3.Session(
        aws_access_key_id=Variable.get('ACCESS_KEY'),
        aws_secret_access_key=Variable.get('SECRET_KEY'),
        region_name='eu-central-1'
        )
    date_str = datetime.today().strftime('%Y-%m-%d')
    path=f's3://chizoba-severe-weather-data/weather_api_data/{date_str}.parquet'
    wr.s3.to_parquet(
        df=df,
        path= path,
        dataset=False,
        boto3_session=session
    )
    return df
    