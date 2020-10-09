from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^especialidades/$', views.EspecialidadeList.as_view(), name='esp-list'),
    url(r'^medicos/$', views.MedicoList.as_view(), name='med-list'),
]