from django.urls import path
from user.views import SignupView, LoginView, profile


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),

]
