"""Main URLs module."""

from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views
from mercados.users.views import ObtainTokenPairWithUser
from mercados.markets.views.markets import DocumentoPDFView

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('mercados.users.urls', 'users'), namespace='users')),
    path('', include(('mercados.markets.urls', 'markets'), namespace='markets')),
    path('', include(('mercados.world.urls', 'world'))),
    path('token/obtain/', ObtainTokenPairWithUser.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),    
    path('documento/<int:pk>/pdf/', DocumentoPDFView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
