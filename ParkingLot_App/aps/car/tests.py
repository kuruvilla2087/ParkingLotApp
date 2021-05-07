import os
import sys
import django
from django.conf import settings
import pymysql 
pymysql.install_as_MySQLdb()

from datetime import datetime

import pandas as pd
from django.db.models import Q
from car.models import car


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)

sys.path.append(r"/Users/kuru/Desktop/ParkingLot_App/aps")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","aps.settings")
django.setup()


car_val_in = car.objects.filter(Q(status='in') | Q(status='out'))
print(car_val_in)

# Time_val = car.objects.values_list('Time_in', flat=True).get(regno='KA-01-H233-123')

# def cal_parking_fee (parking_duration):
#     fee = 2.5
#     if parking_duration > 60:
#         # Here I subtract 2 because the 1st two 30 minutes
#         # have a fixed fee of 2.5 that we've already set
#         if (parking_duration / 30 - 2) == 0:
#             periods_to_pay = 1
#         else:
#             periods_to_pay = (parking_duration / 30 - 2)
#         fee += periods_to_pay * 1.8
#     return(fee)

# #print(str(datetime.now())[:16])

# # print(str(Time_val))
# d1 = datetime.strptime(str(Time_val)[:16], "%Y-%m-%d %H:%M")
# d2 = datetime.strptime(str(datetime.now())[:16], "%Y-%m-%d %H:%M")

# time_delta = (d2 - d1)
# total_seconds = time_delta.total_seconds()
# minutes = total_seconds/60
# hours = int(total_seconds)
# total_fee = cal_parking_fee(hours)
# print(total_fee)



def clean_car_name(car_no):
      car_model = car.objects.get(regno=car_no)
      print("Car name is:",car_model)
      if car.objects.filter(regno=car_model).exists():
        print("Car name matched")


# clean_car_name('ka-01-H233-123')

# print(car_model)