from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from books.views import BooksViewSet, TagsViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="PixelLibrary Swagger",
        default_version='v1',
        description="Документация к api PixelLibrary",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router = routers.DefaultRouter()
router.register(r'books', BooksViewSet, basename='books')
router.register(r'tags', TagsViewSet, basename='tags')
urlpatterns = [
    path('api/', include(router.urls)),

    path('api/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),

    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path('__debug__/', include("debug_toolbar.urls")),
