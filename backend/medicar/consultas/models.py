from django.db import models
from django.conf import settings
from django.db.models import Q

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


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
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        date = f"{self.dia.day}/{self.dia.month}/{self.dia.year}"
        return f"{self.medico.nome} ({date})"


class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True,blank=True)
    agenda = models.ForeignKey(Agenda, on_delete=models.PROTECT, related_name='consultas')
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now=True)

    def __str__(self):
        date = f"{self.agenda.dia.day}/{self.agenda.dia.month}/{self.agenda.dia.year}"
        if self.cliente is None:
            return f"Dr(a). {self.agenda.medico.nome} livre em {date} às {self.horario}"

        return f"{self.cliente} com Dr(a). {self.agenda.medico.nome} em {date} às {self.horario}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance) 