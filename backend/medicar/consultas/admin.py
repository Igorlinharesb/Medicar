from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Agenda)
admin.site.register(Consulta)
