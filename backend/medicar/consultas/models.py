from django.db import models
from django.conf import settings
# Create your models here.

Cliente = settings.AUTH_USER_MODEL

class Especialidade(models.Model):

    especialidade = models.CharField(max_length=20)

    def __str__(self):
        return self.especialidade
        
class Medico(models.Model):
    nome = models.CharField(max_length=50)
    crm = models.IntegerField()
    email = models.EmailField()
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}, CRM - {self.crm}"


class Agendamento(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    livre = models.BooleanField(default=True)


class Agenda(models.Model):
    medico = models.OneToOneField(Medico, on_delete=models.CASCADE)
    agendamentos = models.ManyToManyField(Agendamento)


class Consulta(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    medico = models.OneToOneField(Medico, on_delete=models.SET_NULL, null=True)
    agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE)

