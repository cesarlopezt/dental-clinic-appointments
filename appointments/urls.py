from django.urls import path, include
from .views import PatientCreateView, ProfileView, PatientListView

urlpatterns = [
    path('', ProfileView.as_view(), name="profile"),
    path('patients/', PatientListView.as_view(), name="patient-list"),
    path('patients/create/', PatientCreateView.as_view(), name="patient-create"),

]
