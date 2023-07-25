from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name= 'home'),
    # path('id/',views.home2, name='home2'),
    # path('d/',views.home3,name='home3'),
    # path('bar/',views.home4, name='Navbar'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('time/',views.database, name='database'),
    path('contactus/',views.contactus, name='contactus'),
    path('qrcode3/',views.qrcode3,name='qrcode3'),
    path('qrcode12/',views.qrcode12, name='qrcode12'),
    path('contactus1',views.contactus1,name='contactus1'),
    path('contact2',views.contact2,name='contact2')
    # path('weather2/', views.weather2, name='weather2'),
    # path('weather1/',views.weather1,name='weather1')

]