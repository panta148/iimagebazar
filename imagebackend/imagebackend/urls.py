from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('api/', include("myapi.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


re_path(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
