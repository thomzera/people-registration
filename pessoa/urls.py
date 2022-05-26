from django.urls import path

from .views import ListaPessoaView, PessoaCreatView

urlpatterns = [
    path('', ListaPessoaView.as_view(), name='pessoa.index'),
    path('novo/', PessoaCreatView.as_view(), name='pessoa.novo')
]
