from django.urls import path
from category.views import CategoryPostsView

urlpatterns = [
    path('<int:pk>/', CategoryPostsView.as_view(), name='category-posts')
]
