"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import markets as markets_views

router = DefaultRouter()
router.register(r'markets', markets_views.MarketViewSet, basename='markets')

urlpatterns = [
    path('', include(router.urls))
]