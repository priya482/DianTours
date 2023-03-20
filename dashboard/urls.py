from django.contrib import admin
from django.urls import path,include
from . import views
# from home import urls

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('addpkg/',views.add_package,name='addpkg'),
    path('profile/',views.profile,name='profile'),

    
]
