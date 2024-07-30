from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136542ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136542", Testconnectors136542ViewSet, basename="testconnectors136542"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
