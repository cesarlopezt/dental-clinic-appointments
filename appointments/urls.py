from django.urls import path, include
from .views import (
    ProfileView, PatientCreateView, PatientListView,
    PatientUpdateView, PatientDetailView, PatientDeleteView,
    DentistListView, AppointmentListView, AppointmentDetailView,
    AppointmentCreateView, AppointmentDeleteView, AppointmentUpdateView
)

urlpatterns = [
    path('', ProfileView.as_view(), name="profile"),
    path('dentists/', DentistListView.as_view(), name="dentist-list"),

    path('patients/', PatientListView.as_view(), name="patient-list"),
    path('patients/create/', PatientCreateView.as_view(), name="patient-create"),
    path('patients/<int:pk>/',
         PatientDetailView.as_view(), name="patient-detail"),
    path('patients/<int:pk>/update/',
         PatientUpdateView.as_view(), name="patient-update"),
    path('patients/<int:pk>/delete/',
         PatientDeleteView.as_view(), name="patient-delete"),

    path('appointments/', AppointmentListView.as_view(), name="appointment-list"),
    path('appointments/create/', AppointmentCreateView.as_view(),
         name="appointment-create"),
    path('appointments/<int:pk>/',
         AppointmentDetailView.as_view(), name="appointment-detail"),
    path('appointments/<int:pk>/update/',
         AppointmentUpdateView.as_view(), name="appointment-update"),
    path('appointments/<int:pk>/delete/',
         AppointmentDeleteView.as_view(), name="appointment-delete"),
]
