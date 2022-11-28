from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import feedback.utils.handlers

urlpatterns = [
  path('feedback/admin/', admin.site.urls),
  path('feedback/rosetta/', include('rosetta.urls')),
  path('feedback/api/feedbacks/', include('feedbacks.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns.append(path('docs/', include('feedback.utils.swagger')))

handler404 = feedback.utils.handlers.handler404
handler500 = feedback.utils.handlers.handler500
