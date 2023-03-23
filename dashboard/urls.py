from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'dashboard'
# from home import urls

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('addpkg/',views.add_package,name='addpkg'),
    path('profile/',views.profile,name='profile'),
    #path('addcustomer/',views.add_customer,name='addcustomer'),
    path('addaddress/',views.add_address,name='addcustomer'),

]
