
from django.contrib import admin
from django.urls import path
from . import views
# from home import views as 

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('registration/',views.register,name='registration'),
    path('about/',views.about,name='about us'),
    path('contact/',views.contact,name='contact us'),
    path('addpkg/',views.add_package,name='add package'),
    path('packages/',views.package,name='packages'),
    path('packages/<str:pkg_id>/',views.packageDetail,name='package details'),

    # path('registration',views.registration,name='registration'),
]
