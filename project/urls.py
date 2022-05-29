from django.contrib import admin
from django.urls import include, path
from pessoa.api import viewsets as pessoasviewsets
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'api', pessoasviewsets.PessoaViewSet, basename="Pessoa")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('pessoas/', include('pessoa.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('peopleapi', include(route.urls)),
]
