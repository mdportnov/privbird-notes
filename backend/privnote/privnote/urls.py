from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import privnote.utils.handlers

urlpatterns = [
  path('admin/', admin.site.urls),
  path('rosetta/', include('rosetta.urls')),
  path('api/notes/', include('notes.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns.append(path('docs/', include('privnote.utils.swagger')))

handler404 = privnote.utils.handlers.handler404
handler500 = privnote.utils.handlers.handler500
