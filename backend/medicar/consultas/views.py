from datetime import date
from datetime import datetime
from django.db.models import Count

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class EspecialidadeList(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        
        queryset=Especialidade.objects.all()
        serializer = EspecialidadeSerializer(queryset, many=True)
        return Response(serializer.data)


class MedicoList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        queryset = Medico.objects.all()
        especialidade = request.query_params.getlist('especialidade')
        nome = request.query_params.get('search')

        if nome is not None:    
            queryset = queryset.filter(nome__icontains=nome)

        if len(especialidade) != 0:
            queryset = queryset.filter(especialidade__id__in=especialidade)

        serializer = MedicoSerializer(queryset, many=True)

        return Response(serializer.data)


class ConsultaList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        queryset = Consulta.objects.all()
        
        # Consultas do usuário logado
        queryset = Consulta.objects.filter(cliente=request.user)

        # Consulta posteriores ao dia atual
        qs1 = queryset.filter(agenda__dia__gt = date.today())

        # Consultas no dia atual em horários futuros
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        qs2 = queryset.filter(agenda__dia=date.today()).filter(horario__gt=current_time)

        queryset = qs2.union(qs1)
        serializer = ConsultaSerializer(queryset, many=True)

        return Response(serializer.data)


class AgendaList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        queryset = Agenda.objects.all()

        # Filtrando Agendas com todos os horários preenchidos
        queryset = queryset.filter(consultas__cliente=None)
        queryset = queryset.annotate(c_count=Count('consultas')).filter(c_count__gt=0)

        # Filtrando datas passadas
        queryset = queryset.filter(dia__gt = date.today())

        # Filtrando por parâmetros passados:
        medico = self.request.query_params.get('medico')
        especialidade = request.query_params.getlist('especialidade')
        data_inicio = self.request.query_params.get('data_inicio')
        data_final = self.request.query_params.get('data_final')
        
        if medico is not None:
            queryset = queryset.filter(medico__id=medico)

        if len(especialidade) != 0:
            queryset = queryset.filter(especialidade__id__in=especialidade)
        
        if data_final is not None:
            queryset = queryset.filter(dia__lt=data_final)

        if data_inicio is not None:
            queryset = queryset.filter(dia__gt=data_inicio)
        
                 
        serializer = AgendaSerializer(queryset, many=True)

        return Response(serializer.data)


'''
Pra fazer:
    - Autenticação
    - Especialidades OK
    - Medicos {
        * Filtro por nome e especialidades
    } OK

    - Consultas de um usuário logado {
        * Filtro excluindo consultas passadas
        * Ordenar por dia e horário
    } OK

    - Listar agendas disponíveis{ (GET /agendas/... )
        * Filtro por id do médico
        * Filtro de 1 ou mais especialidades
        * Por intervalo de data
        * Ordenar por dia e horário
        * Eliminar horários passados e já preenchidos
        * 
    }

    - Marcar consulta para usuário logado {
        * Passar id da agenda e horário
        * Retornar todos os dados do agendamento
    }

    - Desmarcar consulta { (DELETE /consultas/<consulta_id>)
        * Somente se o usuário logado tiver feito a consulta
        * Não é possível desmarcar consulta que nunca foi marcada (id inexistente)
        * Não é possível desmarcar consulta que já ocorreu
    }



'''