from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django import forms
from user.models import User


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomUserCreationForm(UserCreationForm):
    avatar = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'avatar', 'date_of_birth')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'
