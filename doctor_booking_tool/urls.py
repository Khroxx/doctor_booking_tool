"""doctor_booking_tool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.views import *

def redirect_to_admin(request): 
    return redirect('/admin/')

urlpatterns = [
    path('', redirect_to_admin),
    path('admin/', admin.site.urls),
    path('api/patients/', PatientView.as_view(), name='patients'),
    path('api/patients/<int:pk>/', PatientView.as_view(), name='single-patient'),
    path('api/doctors/', DoctorView.as_view(), name='doctors'),
    path('api/doctors/<int:pk>/', DoctorView.as_view(), name='single-doctor'),
    path('api/appointments/', AppointmentView.as_view(), name='appointments'),
    path('api/appointments/<int:pk>/', AppointmentView.as_view(), name='single-appointment'),
    path('api/auth-token/', obtain_auth_token, name='token_auth')
]
