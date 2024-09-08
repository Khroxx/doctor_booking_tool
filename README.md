# doctor_booking_tool

1. Clone
```bash
git clone https://github.com/Khroxx/doctor_booking_tool.git
```

2. Open in Code Editor and run install script <br>
If using Max or Linux in Terminal:<br>
- chmod +x installWithBash.sh <br>
- ./installWithBash.sh <br>
If using Windows/WSL: <br>
- installOnWindows.bat <br>

3. For Documentation (make sure local server is running):
http://127.0.0.1:8000/docs/ <br>

# Usage
GET, POST and DELETE

Use Postman to test the APIs: <br>
- http://127.0.0.1:8000/api/patients/
- http://127.0.0.1:8000/api/doctors/
To use appointments you first have to authenticate: <br>
1. create DjangoUser with Terminal or admin interface
2. POST http://127.0.0.1:8000/api/auth-token with djangoUser username and password in headers to get token
3. with djangoUser credentials and 'Token xxxxx' you can now GET, POST and DELETE Appointments
- You will only get Appointments that are connected to djangoUser through the doctor

# Jobchallenge
Code done in <br>
+ Hours: 3h30m
+ tests 0h35m
+ documentation 0h25m
+ feedback x


insgesamt <br>
4h30m