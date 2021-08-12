from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView
from user.forms import CustomUserCreationForm
from user.models import User


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponse("You are already logged in")
        return super().dispatch(request, *args, **kwargs)


class LoginView(BaseLoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home-page')


class UserProfileView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'user/profile/profile.html'
    extra_context = {'flag': False}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user == self.get_object():
            self.extra_context['flag'] = True
        return super().dispatch(request, *args, **kwargs)


def logout_user(request):
    logout(request)
    return redirect('login')
