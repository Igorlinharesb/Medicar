from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import *
from .serializers import *
# Create your views here.

class EspecialidadeList(APIView):
    
    def get(self, request, format=None):
        
        queryset=Especialidade.objects.all()
        serializer = EspecialidadeSerializer(queryset, many=True)
        return Response(serializer.data)


class MedicoList(APIView):

    def get(self, request, format=None):

        queryset = Medico.objects.all()
        especialidade = self.request.query_params.getlist('especialidade')
        nome = request.query_params.get('search')

        if nome is not None:    
            queryset = queryset.filter(nome__icontains=nome)

        if len(especialidade) != 0:
            queryset = queryset.filter(especialidade__id__in=especialidade)

        serializer = MedicoSerializer(queryset, many=True)

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
    }

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