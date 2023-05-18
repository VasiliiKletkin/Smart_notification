from django.urls import include, path
from rest_framework import routers

from .views import AdModelViewSet

router = routers.DefaultRouter()
router.register(r"ads", AdModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
