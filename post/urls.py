from django.urls import path
from post.views import AddPostView, UserPostListView, PostListView, PostDetail

urlpatterns = [
    path('add/', AddPostView.as_view(), name='add-post'),
    path('list/', UserPostListView.as_view(), name='user-post-list'),
    path('all/', PostListView.as_view(), name='all-post-list'),
    path('detail/<int:pk>', PostDetail.as_view(), name='post-detail'),
]
