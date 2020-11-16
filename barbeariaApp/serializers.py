from barbeariaApp.models import *
from rest_framework.serializers import ModelSerializer


class ServicoSerializer(ModelSerializer):
    class Meta:
        model = Servico
        fields = ['id', 'funcionario', 'tipo_de_corte', 'barba']


class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome']


class CorteSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = ['id', 'tipo_de_corte']


class BarbaSerializer(ModelSerializer):
    class Meta:
        model = Barba
        fields = ['id', 'barba']
