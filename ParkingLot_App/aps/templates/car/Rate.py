import math
rate1 = 5
rate2 = 4
rate3 = 3


m = int(input('Please enter the number of minutes parked: '))

if m <= 60:
  x = m/60
  fee = math.ceil(x) * 5
  print('Parking fee for',m,'minutes is $',fee)

elif m>60 and m<=300:
  x = m/60
  fee = math.ceil(x) * rate2
  print('Parking fee for',m,'minutes is $',fee)

elif m>300:
  x = m/60
  fee = math.ceil(x) * rate3
  print('Parking fee for',m,'minutes is $',fee)

else:
  print('Invalid input')