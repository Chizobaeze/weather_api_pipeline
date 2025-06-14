import pandas as pd
import os
import gspread
import boto3
import awswrangler as wr 
import os
from dotenv import load_dotenv

load_dotenv()

client = gspread.service_account(filename="/home/chizoba_eze/gspread.com/pythonspread-462317-2390047e5151.json")

spreadsheet = client.open("spread.com")

worksheet = spreadsheet.sheet1

# Get all data from the worksheet
rows = worksheet.get_all_values()

"""
Transformation is done on this dictionary 

strip: this is to remove every form of white space in the column dataframe

replace: this is to replace  the empty spaces with underscores 

lower: this is to make all the words lower case 

"""

def mates_name():
    df1 = pd.DataFrame(rows[1:], columns=rows[0])
    record_name = []
    for record in df1.columns:
        record = record.strip().strip('"')
        record = ' '.join(record.split())
        record = record.replace(" ", "_")
        record = record.lower()
        record_name.append(record)
    df1.columns = record_name
    return df1


#print(mates_name())


def aws_session():
    session = boto3.Session(
    aws_access_key_id= os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key= os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name = os.getenv('AWS_DEFAULT_REGION'))
    return session

"""
defining the function to export the results in the dataframe
into the defined bucket path in aws
"""

def gspread_upload():
    wr.s3.to_parquet(
    df=mates_name(),
    path="s3://chizoba-gspread-airflow/spread-zoba/",
    boto3_session=aws_session(),
    mode="append",
    dataset=True
    )
    return