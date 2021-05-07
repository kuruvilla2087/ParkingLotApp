def cal_parking_fee (parking_duration):
    fee = 2.5
    if parking_duration > 60:
        # Here I subtract 2 because the 1st two 30 minutes
        # have a fixed fee of 2.5 that we've already set
        if (parking_duration / 30 - 2) == 0:
            periods_to_pay = 1
        else:
            periods_to_pay = (parking_duration / 30 - 2)
        fee += periods_to_pay * 1.8
    return(fee)

from datetime import datetime

d1 = datetime.strptime("2015-08-10 19:33:27.653", "%Y-%m-%d %H:%M:%S.%f")
d2 = datetime.strptime("2021-04-28 10:46:46.00", "%Y-%m-%d %H:%M:%S.%f")

time_delta = (d2 - d1)
total_seconds = time_delta.total_seconds()
minutes = total_seconds/60
hours = int(total_seconds)
total_fee = cal_parking_fee(hours)
print(total_fee)