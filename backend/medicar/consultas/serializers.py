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

    class Meta:
        model = Consulta
        fields = ['id', 'agendamento', 'medico']
