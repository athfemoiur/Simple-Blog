from django.urls import path

from post.views import UserPostListView
from user.views import SignupView, LoginView, UserProfileView, logout_user

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('<int:pk>/posts', UserPostListView.as_view(), name='user-post-list'),
    path('logout/', logout_user, name='logout'),
]
