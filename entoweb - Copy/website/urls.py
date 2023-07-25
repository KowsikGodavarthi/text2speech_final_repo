from django.urls import path
from . import views
from .views import home, signup, bookings, gallery, registerent, registercust, aboutus, contactus, login, welcome, \
    signup2, logout
from django.contrib import admin

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('welcome-to-ent-o-web/', signup2, name='signup2'),
    path('bookings/',bookings, name='bookings'),
    path('gallery/', gallery, name='gallery'),
    path('registerentertainer/', registerent, name='regent'),
    path('registercustomer/', registercust, name='regcus'),
    path('aboutus/', aboutus, name='about'),
    path('contactus/', contactus, name='contactus'),
    path('login/', login, name='login'),
    path('welcome/',welcome, name='welcome'),
    path('logout/',logout,name='logout'),
]
admin.site.site_header = 'ENT-O-WEB ADMIN'
admin.site.index_title = 'Features area'
admin.site.site_title = 'ADMINISTRATION'