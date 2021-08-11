from django.urls import path
from user.views import SignupView, login

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', login, name='login'),
]
