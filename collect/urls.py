from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollectViewSet

router = DefaultRouter()
router.register(r'collects', CollectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test/', lambda request: None),
]