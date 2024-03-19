from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include, re_path

static_urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve,
            {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve,
            {"document_root": settings.STATIC_ROOT}),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.library.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),

    path("", include(static_urlpatterns)),
]
