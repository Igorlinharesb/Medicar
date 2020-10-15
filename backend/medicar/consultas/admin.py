from django.contrib import admin
from .models import *

class ConsultaAdmin(admin.ModelAdmin):

    list_display = ['agenda', 'horario', 'cliente', 'medico']

    class Meta:
        model = Consulta
        fields = ['cliente', 'agenda']
        sorted = ['agenda.dia']


admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Agenda)
admin.site.register(Consulta, ConsultaAdmin)
