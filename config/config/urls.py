from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apiv1.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
