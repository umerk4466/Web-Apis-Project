from django.shortcuts import render
from django.http import HttpResponse
# rest api imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
# serializers
from mot_app.serializers import UserSerializer
from mot_app.serializers import VehicleSerializer
from mot_app.serializers import ReminderSerializer




# import models
from mot_app.models import User
from mot_app.models import Vehicle
from mot_app.models import Reminder


# Create your views here.
def hello(request):
    html = "<html><body>api viewer </body></html>"
    return HttpResponse(html)


################################## USER API FUNCTIONS ##################################################


@api_view(['GET'])
def get_user_data(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = User.objects.filter(username__iexact=username, password__iexact=password).first()
        if not user:
            return Response(data={'message':"UserDoesNotExist"})
        else:
            serializer = UserSerializer(user)
            return Response(serializer.data)
# url : http://127.0.0.1:8000/api/get/user/?username=umer&password=umer

@api_view(['POST'])
def set_user_data(request):
    if request.method == 'POST':
        post_username = request.GET.get('username')
        post_password = request.GET.get('password')
        post_reg_no = request.GET.get('reg_no')
        user_exist = User.objects.filter(username__iexact=post_username).first()
        if user_exist:
            return Response(data={'message':"UserAlreadyExist"})
        else:
            data = {'username': post_username, 'password': post_password , 'current_vehicle_reg_no': post_reg_no,}
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'message':"UserCreatedSuccessfully"})
    return Response(data={'message':"Error"})
#url : http://127.0.0.1:8000/api/register/user/?username=umer&password=!pass123&reg_no=abc92

@api_view(['POST'])
def update_user_data(request):
    if request.method == 'POST':
        post_username = request.GET.get('username')
        post_password = request.GET.get('password')
        post_reg_no = request.GET.get('reg_no')
        post_fname = request.GET.get('fname')
        post_email = request.GET.get('email')

        user_exist = User.objects.filter(username__iexact=post_username, password__iexact=post_password).first()
        if user_exist:
            data = {'username': post_username, 'password': post_password , 'current_vehicle_reg_no': post_reg_no, 'full_name':post_fname, 'email': post_email,}
            serializer = UserSerializer(user_exist, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'message':"UserUpdatedSuccessfully"})
        if not user_exist:
            return Response(data={'message':"UsernameOrPassIncorrect"})
    return Response(data={'message':"Error"})
# url : http://127.0.0.1:8000/api/update/user/?username=umer&password=umer&reg_no=abc92&fname=djdj&email=hsdisd@gmail.com

################################## VEHICLE API FUNCTIONS ##################################################

@api_view(['GET'])
def get_user_vehicle(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        user = User.objects.filter(username__iexact=username).first()
        if not user:
            return Response(data={'message':"UserDoesNotExist"})
        else:
            vehicles = Vehicle.objects.filter(owner=user.id)
            serializer = VehicleSerializer(vehicles,many=True,)
            return Response(serializer.data)
# url : http://127.0.0.1:8000/api/get/user/vehicle/?username=umer



@api_view(['GET'])
def get_vehicle(request):
    if request.method == 'GET':
        vehicle_id = request.GET.get('vehicle_id')
        vehicle = Vehicle.objects.filter(pk=vehicle_id).first()
        if not vehicle:
            return Response(data={'message':"VehicleDoesNotExist"})
        else:
            serializer = VehicleSerializer(vehicle)
            return Response(serializer.data)
# url : http://127.0.0.1:8000/api/get/vehicle/?vehicle_id=1


@api_view(['POST'])
def add_vehicle(request):
    if request.method == 'POST':
        owner_username = request.GET.get('username')
        manufacturer = request.GET.get('manufc')
        millage =request.GET.get('millage')
        condition =request.GET.get('condition')
        reg_year =request.GET.get('reg_year')
        reg_number =request.GET.get('reg_number')
        mot_date =request.GET.get('mot_date')
        mot_due =request.GET.get('mot_due')
        insurance_due =request.GET.get('ins_due')
        note =request.GET.get('note')
        repair_needed =request.GET.get('repair_needed')

        if owner_username and manufacturer and millage and reg_year and reg_number and mot_due and insurance_due:
            user = User.objects.filter(username__iexact=owner_username).first()
            data = {'owner': user.id, 'manufacturer': manufacturer , 'millage': millage, 'condition': condition,'registration_year': reg_year,'registration_number': reg_number,'last_mot_date': mot_date,'mot_due': mot_due, 'insurance_due': insurance_due,'vehicle_notes': note,'repair_needed_note': repair_needed,}
            serializer = VehicleSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'message':"VehicleAddedSuccessfully"})
        else:
            return Response(data={'message':"FillRequiredFields"})
    return Response(data={'message':"Error"})
        
# url : http://127.0.0.1:8000/api/add/vehicle/?username=20&manufc=ford&millage=200&reg_year=2019&reg_number=202jd&mot_due=2091&ins_due=2019


@api_view(['POST'])
def remove_vehicle(request):
    if request.method == 'POST':
        vehicle_id = request.GET.get('vehicle_id')
        vehicle = Vehicle.objects.filter(pk=vehicle_id).first()
        if not vehicle:
            return Response(data={'message':"VehicleDoesNotExist"})
        else:
            vehicle.delete()
            return Response(data={'message':"VehicleRemovedSuccessfully"})
# url : http://127.0.0.1:8000/api/remove/vehicle/?vehicle_id=1


################################## REMINDER API FUNCTIONS ##################################################

@api_view(['GET'])
def get_user_reminder(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        user = User.objects.filter(username__iexact=username).first()
        if not user:
            return Response(data={'message':"UserDoesNotExist"})
        else:
            reminder = Reminder.objects.filter(user=user.id)
            serializer = ReminderSerializer(reminder,many=True,)
            return Response(serializer.data)
# url : http://127.0.0.1:8000/api/get/user/reminder/?username=umer


@api_view(['GET'])
def get_reminder(request):
    if request.method == 'GET':
        reminder_id = request.GET.get('reminder_id')
        reminder = Reminder.objects.filter(pk=reminder_id).first()
        if not reminder:
            return Response(data={'message':"ReminderDoesNotExist"})
        else:
            serializer = ReminderSerializer(reminder)
            return Response(serializer.data)
# url : http://127.0.0.1:8000/api/get/reminder/?reminder_id=1



@api_view(['POST'])
def add_reminder(request):
    if request.method == 'POST':
        user = request.GET.get('username')
        vehicle_id =request.GET.get('vehicle_id')
        reminder_note =request.GET.get('reminder_note')
        date = request.GET.get('date')
        field =request.GET.get('field')


        if user and reminder_note and date:
            user = User.objects.filter(username__iexact=user).first()

            data = {'user': user.id, 'vehicle': vehicle_id , 'reminder_note': reminder_note, 'extra_field': field,'date': date}
            serializer = ReminderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'message':"ReminderAddedSuccessfully"})
        else:
            return Response(data={'message':"FillRequiredFields"})
    return Response(data={'message':"Error"})
# url http://127.0.0.1:8000/api/add/reminder/?username=umer&reminder_note=note is here&date=2019-02-02&vehicle_id=1&field=message


@api_view(['POST'])
def remove_reminder(request):
    if request.method == 'POST':
        reminder_id = request.GET.get('reminder_id')
        reminder = Reminder.objects.filter(pk=reminder_id).first()
        if not reminder:
            return Response(data={'message':"ReminderDoesNotExist"})
        else:
            reminder.delete()
            return Response(data={'message':"ReminderRemovedSuccessfully"})
# url : http://127.0.0.1:8000/api/remove/reminder/?reminder_id=1


@api_view(['POST'])
def update_reminder(request):
    if request.method == 'POST':
        reminder = request.GET.get('reminder_id')
        # vehicle_id =request.GET.get('vehicle_id')
        reminder_note =request.GET.get('reminder_note')
        date = request.GET.get('date')
        field =request.GET.get('field')
        if reminder and date and reminder_note:
            reminder_exist = Reminder.objects.filter(pk=reminder).first()
            if reminder_exist:
                data = {'user': reminder_exist.user.id ,'vehicle' : reminder_exist.vehicle.id ,'reminder_note': reminder_note, 'extra_field': field,'date': date}
                serializer = ReminderSerializer(reminder_exist, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data={'message':"ReminderUpdatedSuccessfully"})
            if not reminder_exist:
                return Response(data={'message':"ReminderIdIncorrect"})
        else:
            return Response(data={'message':"FillRequiredFields"})
    return Response(data={'message':"Error"})

#url http://127.0.0.1:8000/api/update/reminder/?reminder_id=2&reminder_note=hellooloo&date=2029-01-01&field=fielddata