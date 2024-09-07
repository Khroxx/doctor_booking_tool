from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Patient, Doctor, DjangoUser
from django.contrib.auth.hashers import make_password

class PatientTests(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.patient_data = {
            'name': 'John Doe',
            'phone': 1234567890,
            'related_user': self.user
        }
    
    def test_create_patient(self):
        url = reverse('patients')
        patient_data = {
            'name': 'John Doe',
            'phone': 1234567890,
            'related_user': self.user.pk
        }
        response = self.client.post(url, patient_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Patient.objects.get().name, 'John Doe')
        print("POST Patient OK")
    
    def test_get_patients(self):
        Patient.objects.create(**self.patient_data)
        url = reverse('patients')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        print("GET Patient OK")
    
    def test_delete_patient(self):
        patient = Patient.objects.create(**self.patient_data)
        url = reverse('single-patient', args=[patient.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Patient.objects.count(), 0)
        print("DELETE Patient OK")

class DoctorTests(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.doctor_data = {
            'name': 'Bonze',
            'title': 'Dr.',
            'speciality': 'Allgemeinmedizin',
            'related_user': self.user
        }
        
    def test_create_doctor(self):
        url = reverse('doctors')
        doctor_data = {
            'name': 'Bonze',
            'title': 'Dr.',
            'speciality': 'Allgemeinmedizin',
            'related_user': self.user.pk
        }
        response = self.client.post(url, doctor_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Doctor.objects.count(), 1)
        self.assertEqual(Doctor.objects.get().name, 'Bonze')
        print("POST Doctor OK")
    
    def test_get_doctors(self):
        Doctor.objects.create(**self.doctor_data)
        url = reverse('doctors')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        print("GET Doctor OK")
    
    def test_delete_doctor(self):
        doctor = Doctor.objects.create(**self.doctor_data)
        url = reverse('single-doctor', args=[doctor.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Doctor.objects.count(), 0)
        print("DELETE Doctor OK")
        