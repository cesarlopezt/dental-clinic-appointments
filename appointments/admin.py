from django.contrib import admin
from .models import Person, Patient, Dentist, Secretary, Clinic, Appointment

admin.site.site_title = "Clinica odontologica"
admin.site.site_header = "Administrador Clinica Odontologica"

admin.site.register(Person)
admin.site.register(Patient)
admin.site.register(Dentist)
admin.site.register(Secretary)
admin.site.register(Clinic)
admin.site.register(Appointment)
