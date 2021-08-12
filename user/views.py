from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView
from user.forms import CustomUserCreationForm, LoginForm
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
    form_class = LoginForm
    redirect_authenticated_user = True


class UserProfileView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'user/profile/profile.html'


class UpdateProfileView(UpdateView):
    model = User
    template_name = 'user/profile/edit-profile.html'
    fields = ('username', 'first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('home-page')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != self.kwargs['pk']:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)
