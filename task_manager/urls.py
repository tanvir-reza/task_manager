
from django.contrib import admin
from django.urls import path, include ,re_path# new
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
