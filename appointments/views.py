from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy, reverse
from django import forms

from django.contrib.auth.models import User
from .models import Patient, Dentist, Appointment
from .forms import DateInput


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = User
    template_name = 'secretaries/profile.html'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info_navbar'] = "selected"

        ph = self.object.secretary.phone_no
        context['phone'] = f"({ph[0:3]}) {ph[3:6]}-{ph[6:10]}"
        return context


# Dentists
@method_decorator(login_required, name='dispatch')
class DentistListView(ListView):
    model = Dentist
    template_name = 'dentists/list.html'
    context_object_name = 'dentists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dentists_navbar'] = "selected"
        return context


# Patients
@method_decorator(login_required, name='dispatch')
class PatientListView(ListView):
    model = Patient
    template_name = 'patients/list.html'
    context_object_name = 'patients'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients_navbar'] = "selected"
        return context


@method_decorator(login_required, name='dispatch')
class PatientCreateView(CreateView):
    model = Patient
    fields = "__all__"
    template_name = 'patients/create.html'
    success_url = reverse_lazy('patient-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients_navbar'] = "selected"
        return context

    def get_form(self, form_class=None):
        form = super(PatientCreateView, self).get_form(form_class)
        form.fields['birth_date'] = forms.DateField(widget=DateInput)
        return form


@method_decorator(login_required, name='dispatch')
class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patients/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients_navbar'] = "selected"
        return context


@method_decorator(login_required, name='dispatch')
class PatientUpdateView(UpdateView):
    model = Patient
    fields = "__all__"
    template_name = 'patients/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients_navbar'] = "selected"
        return context

    def get_success_url(self):
        return reverse('patient-detail', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super(PatientUpdateView, self).get_form(form_class)
        form.fields['birth_date'] = forms.DateField(widget=DateInput)
        return form


@method_decorator(login_required, name='dispatch')
class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patients/delete.html'
    success_url = reverse_lazy('patient-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients_navbar'] = "selected"
        return context


# Appointment
@method_decorator(login_required, name='dispatch')
class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/list.html'
    context_object_name = 'appointments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments_navbar'] = "selected"
        return context


@method_decorator(login_required, name='dispatch')
class AppointmentCreateView(CreateView):
    model = Appointment
    fields = "__all__"
    template_name = 'appointments/create.html'
    success_url = reverse_lazy('appointment-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments_navbar'] = "selected"
        return context


@method_decorator(login_required, name='dispatch')
class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointments/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments_navbar'] = "selected"
        return context


@method_decorator(login_required, name='dispatch')
class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = "__all__"
    template_name = 'appointments/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments_navbar'] = "selected"
        return context

    def get_success_url(self):
        return reverse('appointment-detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointments/delete.html'
    success_url = reverse_lazy('appointment-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments_navbar'] = "selected"
        return context
