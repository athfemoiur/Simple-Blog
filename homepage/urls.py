from django.urls import path
from homepage.views import LatestPostListView

urlpatterns = [
    path('', LatestPostListView.as_view(), name='home-page')
]
