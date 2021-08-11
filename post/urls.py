from django.urls import path
from post.views import AddPostView

urlpatterns = [
    path('add/', AddPostView.as_view(), name='add-post')
]
