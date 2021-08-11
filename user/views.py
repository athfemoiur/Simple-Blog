from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from user.forms import CustomUserCreationForm


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
    success_url = reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and request.user.is_authenticated:
            return redirect(self.success_url)
        super().dispatch(request, *args, **kwargs)


@login_required
def profile(request):
    return HttpResponse(f"{request.user.username}")
