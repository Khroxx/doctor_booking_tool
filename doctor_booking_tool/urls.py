"""
doctor_booking_tool URL Configuration
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, re_path
from django.views.static import serve
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
    path('api/auth-token/', obtain_auth_token, name='token_auth'),
    re_path(r'^docs/(?P<path>.*)$', docs_serve),
]
