from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.views.generic.detail import DetailView

from django.contrib.auth.models import User
from .models import Secretary


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_object(self):
        return self.request.user


# def get_context_data(self, **kwargs):
#     context = super(ProfileView, self).get_context_data(**kwargs)
#     context['post_list'] = Post.objects.filter(user__username__iexact=self.kwargs.get('username'))
#     return context
