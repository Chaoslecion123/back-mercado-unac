"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import markets as markets_views

router = DefaultRouter()
router.register(r'markets', markets_views.MarketViewSet, basename='markets')
router.register(r'countermarket', markets_views.CounterMarketViewSet, basename='counter-market')
router.register(r'pass_mercado', markets_views.MarketPassRequestViewSet, basename='market-pass-request')

urlpatterns = [
    path('', include(router.urls)),
]