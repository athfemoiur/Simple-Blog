from django.urls import path
from homepage.views import home_page

urlpatterns = [
    path('', home_page, name='home-page')
]
