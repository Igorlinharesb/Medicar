from rest_framework import serializers
from .models import *


class EspecialidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialidade
        fields = '__all__'
    # Sem necessidade de validação


class MedicoSerializer(serializers.ModelSerializer):

    especialidade = EspecialidadeSerializer()

    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'especialidade']


class ConsultaSerializer(serializers.ModelSerializer):

    medico = MedicoSerializer()
    dia = serializers.CharField(source='agenda.dia', read_only=True)

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']


class AgendaSerializer(serializers.ModelSerializer):

    medico = MedicoSerializer()

    class Meta:
        model = Agenda
        fields = ['id', 'dia', 'medico', 'consultas']


