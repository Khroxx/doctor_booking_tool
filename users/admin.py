from django.contrib import admin
from users.models import *

# Register your models here.

# class Patient(admin.ModelAdmin):
admin.site.register(DjangoUser)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)

