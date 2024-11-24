from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from movies_app.views import request_count, request_count_reset

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("movies_app.urls")),
    path("request-count/", request_count),
    path("request-count/reset/", request_count_reset),
    path("docs/", include("project.urls.docs")),
]
