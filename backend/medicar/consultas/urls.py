from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include


urlpatterns = [
    url(r'^especialidades/$', views.EspecialidadeList.as_view(), name='esp-list'),
    url(r'^medicos/$', views.MedicoList.as_view(), name='med-list'),
    url(r'^consultas/$', views.ConsultaList.as_view(), name='cons-list'),
    url(r'^agendas/$', views.AgendaList.as_view(), name='agenda-list'),
]

urlpatterns += [
    path('api-token-auth/', obtain_auth_token)
]