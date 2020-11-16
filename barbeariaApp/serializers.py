from barbeariaApp.models import *
from rest_framework.serializers import ModelSerializer


class ServicoSerializer(ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'


class CorteSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = '__all__'


class BarbaSerializer(ModelSerializer):
    class Meta:
        model = Barba
        fields = '__all__'
