"""
URL configuration for configuration project.
"""

from django.contrib import admin
from django.urls import path, include
from oauth2_provider import urls as oauth2_urls
from .api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
]
