from django.shortcuts import render
from django.http import HttpResponse
from car.models import car,parking
from car.forms import NewCarForm, RemoveCarForm, SearchCarForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q


@login_required
def index(request):
    parking_val = parking.objects.order_by('level')

    final_val = { 'parkval': parking_val,}
    return render(request, 'car/index.html', context= final_val)

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

def parkingfunc(request):
    error_msg = 0
    msg = 0
    delform = RemoveCarForm()
    car_val_in = car.objects.filter(Q(status='in') | Q(status='out'))
    if 'deleting' in request.POST:
        if request.method == "POST":
            delform = RemoveCarForm(request.POST)
            if delform.is_valid():
                slot_val = 0
                level_val = 0
                formregno = delform.cleaned_data['regno']
                reg_car = car.objects.filter(regno = formregno, status = 'in')
                for regcar in reg_car:
                    slot_val = regcar.slot
                    level_val = regcar.level
                    Time_val = regcar.Time_in
                park_slot_query = parking.objects.filter(level = level_val)
                if slot_val == 1 :
                    msg = 101
                    park_slot_query.update(slot1 = 0)
                elif slot_val == 2:
                    msg = 101
                    park_slot_query.update(slot2 = 0)
                elif slot_val == 3:
                    msg = 101
                    park_slot_query.update(slot3 = 0)
                elif slot_val == 4:
                    msg = 101
                    park_slot_query.update(slot4 = 0)

                if msg == 101:
                    d1 = datetime.strptime(str(Time_val)[:16], "%Y-%m-%d %H:%M")
                    d2 = datetime.strptime(str(datetime.now())[:16], "%Y-%m-%d %H:%M")
                    time_delta = (d2 - d1)
                    total_seconds = time_delta.total_seconds()
                    minutes = total_seconds/60
                    hours = int(total_seconds)
                    total_fee = cal_parking_fee(hours)
                    reg_car.update(slot=999, level=999, status = 'out',Date_out = d2,Charged_price=total_fee)
                else:
                    error_msg = 101
   


    form = NewCarForm()
    park_val = parking.objects.order_by('level')
    if 'adding' in request.POST:
        if request.method == "POST":
            form = NewCarForm(request.POST)
            if form.is_valid():
                formregno = form.cleaned_data['regno']

                level = 1
                for park in park_val:
                    parkslot = parking.objects.filter(level=level)
                    if park.slot1 == 0:
                        form.save(commit=True)
                        parkslot.update(slot1 = 1)
                        car.objects.filter(regno=formregno).update(slot= 1, level=level)
                        msg = 100
                        break
                    elif park.slot2 == 0:
                        form.save(commit=True)
                        parkslot.update(slot2 = 1)
                        car.objects.filter(regno=formregno).update(slot=2, level=level)
                        msg = 100
                        break
                    elif park.slot3 == 0:
                        form.save(commit=True)
                        parkslot.update(slot3 = 1)
                        car.objects.filter(regno=formregno).update(slot = 3, level=level)
                        msg = 100
                        break
                    elif park.slot4 == 0:
                        form.save(commit=True)
                        parkslot.update(slot4 = 1)
                        car.objects.filter(regno=formregno).update(slot = 4, level=level)
                        msg = 100
                        break
                    else:
                        level = level+1

                if msg != 100:
                    error_msg = 100
            # return index(request)

    return render(request,'car/parking.html', {'form':form, 'delform':delform, 'carvalin':car_val_in, 'errormsg' : error_msg , 'msg' : msg})

def searchfunc(request):
    final_val = {}
    searchform = SearchCarForm()
    if request.method == "GET":
        searchform = SearchCarForm(request.GET)
        if searchform.is_valid():
            search_val = searchform.cleaned_data['searchfield']

            color_search = car.objects.filter(color=search_val).order_by('-id')
            reg_no_search = car.objects.filter(regno=search_val).order_by('-id')
            for reg in reg_no_search:
                print (reg.color)
            final_val = { 'searchform':searchform,'reg_no_search':reg_no_search , 'color_search': color_search}
            print("final val")
            print (final_val)
    return render(request, 'car/search.html', context= final_val)
