from django.contrib import admin
from django.urls import include, path

import privbird.utils.handlers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/notes/', include('notes.urls')),
    path('api/feedbacks/', include('feedbacks.urls'))
]

handler404 = privbird.utils.handlers.handler404
handler500 = privbird.utils.handlers.handler500
