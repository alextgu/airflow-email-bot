import os
import requests

import random
from airflow import DAG
from airflow.operators.email_operator import EmailOperator

from datetime import datetime


default_args = {
    'owner': 'TGu',
    'depends_on_past': False,
    'start_date': datetime(2020, 6, 6),
    'retries': 0,
}


def generate_email():
    email = ['Email to send to friend 1', 'Email to send to friend 2']
    return random.choice(email)    


with DAG(
    'Send Email to friends',
    default_args=default_args,
    schedule_interval='*/5 * * * *',
    catchup=False,
) as dag:
    email_friend = EmailOperator(
        task_id='email_friend',
        to='zhangqiuxiao@hotmail.com',
        subject='this is an automated message from TGU',
        html_content='<h3>{}</h3>'.format(generate_email())
    )
