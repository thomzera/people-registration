from pessoa import models
from pyexpat import model
from rest_framework import serializers


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoa
        fields = '__all__'
