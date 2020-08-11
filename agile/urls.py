from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AgileViewSet

app_name = "agile"


router = DefaultRouter()
router.register("agile", AgileViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
