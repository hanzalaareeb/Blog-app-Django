from django.urls import path
from .views import home_page_view
from .api import api

# code goes here

urlpatterns = [
    path("", home_page_view, name="home"),
    path("api/", api.urls),
]
