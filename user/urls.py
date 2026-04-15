from django.urls import path
from .api import api

# code goes here

urlpatterns = [
    path("api/", api.urls),
]
