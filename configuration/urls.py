"""
URL configuration for configuration project.
"""

from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),  # new
    path("api/", api.urls),
]
