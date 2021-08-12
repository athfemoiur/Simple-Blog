from django.urls import path
from post.views import AddPostView, UserPostListView, PostListView, PostDetail, UpdatePostView, DeletePostView

urlpatterns = [
    path('add/', AddPostView.as_view(), name='add-post'),
    path('all/', PostListView.as_view(), name='all-post-list'),
    path('detail/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('edit/<int:pk>', UpdatePostView.as_view(), name='edit-post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
]
