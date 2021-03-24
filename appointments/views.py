from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from django.contrib.auth.models import User
from .models import Patient, Dentist


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = User
    template_name = 'secretaries/profile.html'

    def get_object(self):
        return self.request.user


# Dentists
@method_decorator(login_required, name='dispatch')
class DentistListView(ListView):
    model = Dentist
    template_name = 'dentists/list.html'
    context_object_name = 'dentists'


# Patients
@method_decorator(login_required, name='dispatch')
class PatientListView(ListView):
    model = Patient
    template_name = 'patients/list.html'
    context_object_name = 'patients'


@method_decorator(login_required, name='dispatch')
class PatientCreateView(CreateView):
    model = Patient
    fields = "__all__"
    template_name = 'patients/create.html'
    success_url = reverse_lazy('patient-list')


@method_decorator(login_required, name='dispatch')
class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patients/detail.html'


@method_decorator(login_required, name='dispatch')
class PatientUpdateView(UpdateView):
    model = Patient
    fields = "__all__"
    template_name = 'patients/update.html'
    success_url = reverse_lazy('patient-list')


@method_decorator(login_required, name='dispatch')
class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patients/delete.html'
    success_url = reverse_lazy('patient-list')
