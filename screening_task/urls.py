"""screening_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from drf_yasg.views import get_schema_view  # type: ignore
from drf_yasg import openapi  # type: ignore
from rest_framework import permissions

urlpatterns = [
    path("api/", include("agile.urls", namespace="agile")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="LASSI API",
        default_version="v1",
        description="LASSI API Documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path(
        "api-docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
