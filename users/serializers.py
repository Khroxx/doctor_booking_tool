from rest_framework import serializers
from .models import *
    
    
class PatientSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Patient
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True}
        }
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True},
            'title': {'required': True},
            'speciality': {'required': True},
            
        }
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        extra_kwargs = {
            'title': {'required': True},
            'has_patient': {'required': True},
            'has_doctor': {'required': True},
            'date': {'required': True},
        }