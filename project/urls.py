from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('pessoas/', include('pessoa.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
