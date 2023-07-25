from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username'],
        password=request.POST['password'],
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('welcome')
        return redirect('login')
    return render(request, 'Login.html')

def signup(request):
    return render(request, 'signup.html')
def signup2(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # tosend = f'Hi {username}, Thank You for Registering in Epc Portal,We look forward to serving You'
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # send_mail('Registration Successful', tosend, 'manishbabusujanimulk17@gmail.com', [mail])

        return render(request, 'welcome.html')
    else:
        return HttpResponse("INCORRECT")
def gallery(request):
    return render(request, 'gallery.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def bookings(request):
    return render(request, 'bookings.html')
def contactus(request):
    return render(request, 'contactus.html')
def registercust(request):
    return render(request, 'Register_Customer.html')
def registerent(request):
    return render(request, 'Register_Entertainer.html')

def logout(request):
    redirect('login')