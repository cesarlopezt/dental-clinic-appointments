from django.urls import path, include
from .views import ProfileView

urlpatterns = [
    path('', ProfileView.as_view(), name="profile"),
]
