from django.urls import path
from post.views import UserPostListView
from user.views import SignupView, LoginView, UserProfileView, UpdateProfileView
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='profile'),
    path('<int:pk>/profile-edit', UpdateProfileView.as_view(), name='profile-edit'),
    path('<int:pk>/posts/', UserPostListView.as_view(), name='user-post-list'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset-password', PasswordResetView.as_view(template_name='user/reset-password/reset_password.html'),
         name='reset_password'),
    path('reset-password-sent',
         PasswordResetDoneView.as_view(template_name='user/reset-password/reset_password_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(template_name='user/reset-password/reset_password_confirm.html'),
         name='password_reset_confirm'),
    path('reset-password-change',
         PasswordResetCompleteView.as_view(template_name='user/reset-password/reset_password_complete.html'),
         name='password_reset_complete')
]
