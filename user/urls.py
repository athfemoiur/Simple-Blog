from django.urls import path

from post.views import UserPostListView
from user.views import SignupView, LoginView, UserProfileView, UpdateProfileView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='profile'),
    path('<int:pk>/profile-edit', UpdateProfileView.as_view(), name='profile-edit'),
    path('<int:pk>/posts/', UserPostListView.as_view(), name='user-post-list'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
