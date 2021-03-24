from django.urls import path, include
from .views import (ProfileView, PatientCreateView, PatientListView,
                    PatientUpdateView, PatientDetailView, PatientDeleteView,
                    DentistListView
                    )

urlpatterns = [
    path('', ProfileView.as_view(), name="profile"),
    path('dentists/', DentistListView.as_view(), name="dentist-list"),
    path('patients/', PatientListView.as_view(), name="patient-list"),
    path('patients/create/', PatientCreateView.as_view(), name="patient-create"),
    path('patients/<int:pk>/detail/',
         PatientDetailView.as_view(), name="patient-detail"),
    path('patients/<int:pk>/update/',
         PatientUpdateView.as_view(), name="patient-update"),
    path('patients/<int:pk>/delete/',
         PatientDeleteView.as_view(), name="patient-delete"),

]
