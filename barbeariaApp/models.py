from django.db import models

funcionarios = [
    ('José', 'José'),
    ('Pedro', 'Pedro'),
    ('PH', 'PH')
]

cortes = [
    ('Social', 'Social'),
    ('Degradê', 'Degradê')
]

barba = [
    ('Com Barba', 'Com Barba'),
    ('Sem Barba', 'Sem Barba')
]


class Servico(models.Model):
    funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    tipo_de_corte = models.ForeignKey(
        'Corte', on_delete=models.CASCADE)
    barba = models.ForeignKey('Barba', on_delete=models.CASCADE)

    def __str__(self):
        return self.funcionario.nome

    class Meta:
        verbose_name = ("Serviço")
        verbose_name_plural = ("Serviços")


class Funcionario(models.Model):
    nome = models.CharField('Nome', choices=funcionarios, max_length=50)

    def __str__(self):
        return self.nome


class Corte(models.Model):
    tipo_de_corte = models.CharField('Cortes', choices=cortes, max_length=10)

    def __str__(self):
        return self.tipo_de_corte


class Barba(models.Model):
    barba = models.CharField('Barba', choices=barba, max_length=10)

    def __str__(self):
        return self.barba
