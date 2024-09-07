from django.shortcuts import render
from rest_framework.authtoken.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404



# Create your views here.

class PatientView(APIView):
    def get(self, request, format=None):
        patients =  Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Patient has been created'})
    
    
    def delete(self, request, pk, *args, **kwargs):
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return Response({'message': 'Patient has been deleted'})
    
    
class DoctorView(APIView):
    def get(self, request, format=None):
        doctors =  Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Doctor has been created'})
        
    
    
    def delete(self, request, pk, *args, **kwargs):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response({'message': 'Doctor has been deleted'})
    
    
class AppointmentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        djangoUser = get_object_or_404(Doctor, related_user=request.user)
        appointments =  Appointment.objects.filter(has_doctor=djangoUser)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = AppointmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Appointment has been created'})
    
    
    def delete(self, request, pk, *args, **kwargs):
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.delete()
        return Response({'message': 'Appointment has been deleted'})