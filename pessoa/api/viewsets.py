from pessoa import models
from pessoa.api import serializers
from rest_framework import viewsets


class PessoaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PessoaSerializer
    queryset = models.Pessoa.objects.all()
