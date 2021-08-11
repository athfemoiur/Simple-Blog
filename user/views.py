from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import DetailView
from user.forms import CustomUserCreationForm
from user.models import User


class SignupView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().get(request, *args, **kwargs)


class LoginView(BaseLoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('profile')


class UserProfileView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'user/profile/profile.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user
