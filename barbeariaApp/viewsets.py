from rest_framework import viewsets
from barbeariaApp.models import *
from barbeariaApp.serializers import *


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class CorteViewSet(viewsets.ModelViewSet):
    queryset = Corte.objects.all()
    serializer_class = CorteSerializer


class BarbaViewSet(viewsets.ModelViewSet):
    queryset = Barba.objects.all()
    serializer_class = BarbaSerializer
