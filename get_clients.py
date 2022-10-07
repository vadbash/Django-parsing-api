import os
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()
from django.core.management.base import BaseCommand
from clients.models import ClientsList, NoActiveClientsList, NotActivePositiveBalance
import requests
import json


url = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=clients"
res = requests.get(url)
data = res.json()

for i in range(len(data)):
    save_clients = ClientsList(full_name=data[i]['full_name'], email = data[i]['email'], address = data[i]['address'],
                phone_number = data[i]['phone_number'], current_balance = data[i]['current_balance'], last_payment = data[i]['last_payment'],
                reg_date = data[i]['reg_date'], lastcall_date = data[i]['lastcall_date'], status = data[i]['status'])
    save_clients.save()


for i in range(len(data)):
    client = ClientsList.objects.get(id=(i+1))
    if client.status == False:
            save_not_active_client = NoActiveClientsList(full_name=data[i]['full_name'], email = data[i]['email'], address = data[i]['address'],
                phone_number = data[i]['phone_number'], current_balance = data[i]['current_balance'], last_payment = data[i]['last_payment'],
                reg_date = data[i]['reg_date'], lastcall_date = data[i]['lastcall_date'], status = data[i]['status'])
            save_not_active_client.save()


for i in range(len(data)):
    client = ClientsList.objects.get(id=i+1)
    if client.current_balance > 0 and client.status == False:
            not_active_but_positive_balance_client = NotActivePositiveBalance(full_name=data[i]['full_name'], email = data[i]['email'], address = data[i]['address'],
                phone_number = data[i]['phone_number'], current_balance = data[i]['current_balance'], last_payment = data[i]['last_payment'],
                reg_date = data[i]['reg_date'], lastcall_date = data[i]['lastcall_date'], status = data[i]['status'])
            not_active_but_positive_balance_client.save()