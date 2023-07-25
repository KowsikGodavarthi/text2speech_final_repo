import datetime
import time

from django.contrib.auth.models import User
from django.core.mail import send_mail
from pymongo import auth

from .models import date
from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from django.http import FileResponse

# Create your views here.
# def home(request):
#     return HttpResponse("Hello world")
# def home2(request):
#     return HttpResponse("2100030708 ")
# def home3(request):
#     return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def contactus(request):
    return render(request, 'contactus.html')
def contact2(request):
    return render(request, 'contact2.html')

def database(request):
    variable1 = time.asctime(time.localtime(time.time()))
    data =date(time12=variable1)
    data.save()
    return HttpResponse(variable1)

#
# def weather21(request):
#     return render(request,'weather2.html')
#
# import requests
# def weather1(request):
#
#    if request.method == 'POST':
#         api_key = '359dbceb79d7268b74433b2a8dc9dd0b'
#         user_input = request.POST.get('city')
#
#         weather_data = requests.get(
#         f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
#
#    if weather_data.json()['cod'] == '404':
#         return HttpResponse('Data Failure')
#    else:
#
#         weather = weather_data.json()['weather'][0]['main']
#         temp = round(weather_data.json()['main']['temp'])
#         temp1 = (((temp - 32) * 5) / 9)
#         return render(request,'weather.html',locals())


def qrcode3(request):
    return render(request, 'Qrcode.html')


def qrcode12(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        sname = request.POST.get('sname')
        data = sid + sname

        qr = qrcode.QRCode(version=1, box_size=30, border=5)

        qr.add_data(data)

        qr.make(fit=True)

        img = qr.make_image(fill_color='black', back_color='white')

        img.save('fetcheddata.png')

        img1 = open('fetcheddata.png', 'rb')

        response = FileResponse(img1)

        return response

    else:
        return HttpResponse("Not Working")
#
def contact12(request):
    return render(request,'contactus.html')
def contactus1(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment + '___________This is just the comment line'

        data = contactus(firstname = firstname, lastname = lastname, email = email)

        data.save()
        send_mail(
            'Thank You for Contacting EPS system',
            tosend,
            'sreekarpalanati27@gmail.com'
            [email],

        )

def login(request):
    return render(request,'login.html')


def login2(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = auth.authenticate(username = username,password = password)

        if user is not None :
            auth.login(request,user)
            return render(request,'Home.html')
        else:
            return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def register2(request):
    if request.method == "POST":
        username = request.POST.get('username')
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        tosend = f'Hi {username}, Thank You for Registering in Epc Portal,We look forward to serving You'
        user = User.objects.create_user(username=username,email=mail,password=password)
        user.save()

        send_mail('Registration Successful' ,tosend ,'manishbabusujanimulk17@gmail.com' ,[mail])

        return render(request,'login.html')
    else:
        return HttpResponse("INCORRECT")