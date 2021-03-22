from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_card = models.CharField(max_length=11, null=True)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=75)
    birth_date = models.DateField()
    registration_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "People"


class Clinic(models.Model):
    name = models.CharField(max_length=30)
    rnc = models.CharField(max_length=9)

    def __str__(self) -> str:
        return self.name


class Dentist(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.person.first_name} {self.person.last_name}"


class Secretary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.person.first_name} {self.person.last_name}"

    class Meta:
        verbose_name_plural = "Secretaries"


class Patient(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    def __str__(self) -> str:
        return f"{self.person.first_name} {self.person.last_name}"

    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='Active')


class Appointment(models.Model):
    REASON = (
        ('CG', 'Consulta General'),
        ('LD', 'Limpieza Dental'),
        ('OR', 'Ortodoncia'),
        ('EX', 'Extracción'),
        ('RX', 'Radiografías'),
    )
    PAYMENT_METHOD = (
        ('CS', 'Cash'),
        ('DC', 'Debit Card'),
        ('CC', 'Credit Card')
    )

    appointment_reason = models.CharField(
        max_length=2, choices=REASON, default='CG')
    payment_method = models.CharField(
        max_length=2, choices=PAYMENT_METHOD, default='CS')
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self) -> str:
        patient = self.patient.person
        patient_name = f"{patient.first_name} {patient.last_name}"
        date = f"{self.date.date()} | {self.date.strftime('%H:%M')}"
        return f"{date}: {self.appointment_reason} -> {patient_name}"
