from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from user.forms import CustomUserCreationForm


class SignupView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def login(request):
    return HttpResponse("Login page")
