from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_card = models.CharField(max_length=11, null=True)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=75)
    birth_date = models.DateField()
    birth_date = models.DateTimeField()


class Clinic(models.Model):
    name = models.CharField(max_length=30)
    rnc = models.CharField(max_length=9)


class Dentist(models.Model):
    person = models.OneToOneField(Person)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)


class Secretary(models.Model):
    person = models.OneToOneField(Person)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)


class Patient(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    person = models.OneToOneField(Person)
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
