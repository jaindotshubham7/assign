from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path("manage/", admin.site.urls),
    path("api/", include("videos.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
