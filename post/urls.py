from django.urls import path
from post.views import AddPostView, UserPostList

urlpatterns = [
    path('add/', AddPostView.as_view(), name='add-post'),
    path('list/', UserPostList.as_view(), name='user-post-list'),
]
