from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import PessoaForm
from .models import Pessoa

# Create your views here.


class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')


class PessoaCreatView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'


class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'


class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'
