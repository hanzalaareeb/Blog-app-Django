from django.urls import path
from .views import home_page_view

# code goes here

urlpatterns = [
    path("", home_page_view, name="home"),
]
