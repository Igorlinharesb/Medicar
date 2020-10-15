from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include


urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('especialidades/', views.EspecialidadeList.as_view(), name='esp-list'),
    path('medicos/', views.MedicoList.as_view(), name='med-list'),
    path('consultas/', views.ConsultaList.as_view(), name='cons-list'),
    path('consulta/<int:consulta_id>', views.ConsultaDetail.as_view(), name='delete-consulta'),
    path('agendas/', views.AgendaList.as_view(), name='agenda-list'),
]
