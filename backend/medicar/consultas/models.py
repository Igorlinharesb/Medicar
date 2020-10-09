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


class Agenda(models.Model):
    dia = models.DateField()
    medico = models.OneToOneField(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return f"Agenda de {self.medico.nome}"


class Consulta(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.SET_NULL, null=True)
    agenda = models.ForeignKey(Agenda, on_delete=models.PROTECT)
    horario = models.TimeField()

    def __str__(self):
        return f"{self.cliente} com Dr(a). {self.medico} em {self.agenda.dia} às {self.horario}"
