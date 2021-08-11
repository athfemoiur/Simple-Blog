from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'date_of_birth')
        widgets = {'date_of_birth': DateInput()}
