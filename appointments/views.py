from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from django.contrib.auth.models import User
from .models import Patient


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = User
    template_name = 'secretaries/profile.html'

    def get_object(self):
        return self.request.user


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

# def get_context_data(self, **kwargs):
#     context = super(ProfileView, self).get_context_data(**kwargs)
#     context['post_list'] = Post.objects.filter(user__username__iexact=self.kwargs.get('username'))
#     return context
