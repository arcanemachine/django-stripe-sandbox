from django.contrib import admin
from django.urls import include, path

from stripes import views as stripes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stripes.urls')),
]
