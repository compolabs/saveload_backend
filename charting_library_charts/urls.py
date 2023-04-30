from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^1\.0/', include('api.v10.urls')),
    url(r'^1\.1/', include('api.v11.urls')),
    url(r'', include('django_prometheus.urls')),
    url(r'^admin/', admin.site.urls),
]
