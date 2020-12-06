from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views

admin.site.site_header = "Fazon Admin"
admin.site.site_title = "Fazon Admin Portal"
admin.site.index_title = "Welcome to Fazon"

schema_view = get_schema_view(
    openapi.Info(
        title="Fazon API Documentation",
        default_version='v1',
        description="Fazon Inc.",
        terms_of_service="https://www.held-in.uz/",
        contact=openapi.Contact(email="info@heldin.uz"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='doc'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('events.urls'), name='events'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT) + \
                   static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
