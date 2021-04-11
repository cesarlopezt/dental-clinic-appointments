from django.contrib import admin
from .models import Patient, Dentist, Secretary, Clinic, Appointment

admin.site.site_title = "Dental Clinic"
admin.site.site_header = "Dental Clinic Admin"

admin.site.register(Patient)
admin.site.register(Dentist)
admin.site.register(Secretary)
admin.site.register(Clinic)
admin.site.register(Appointment)
