from django.contrib import admin
from django.urls import include, path, re_path

from drf_yasg.openapi import Info
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    Info(
        title='Note API',
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include('secnote.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^api/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
