from django.urls import path, include
from .views import ProfileView, PatientListView

urlpatterns = [
    path('', ProfileView.as_view(), name="profile"),
    path('patients/', PatientListView.as_view(), name="patient-list"),

]
