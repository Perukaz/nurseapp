from django.contrib import admin
from django.shortcuts import render
from django.urls import path

from .models import Enfermero, Paciente, PacienteChequeo, RitmoCardiaco, \
    PresionSanguinea

# nombre del sitio
admin.site.site_header = "NurseApp"


class ChequeoAdmin(admin.ModelAdmin):
    change_form_template = 'admin/app/diagnostico.html'


# modificacion para que se pueda ver el input para ver la imagen
class PacienteAdmin(admin.ModelAdmin):
    change_list_template = 'admin/app/chequeo_change_list.html'
    list_display = ['nombre', 'apellido']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('estado', self.busqueda, name='busqueda')
        ]
        return custom_urls + urls

    def busqueda(self, request):
        q = request.GET.get('q')
        if request.method == 'POST':
            pass
        else:
            context = {
                'documento': q
            }
        return render(request, 'app/paciente_grafico.html', context)

# se agregan los modelos que se quieren ver
admin.site.register(Enfermero)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(PacienteChequeo, ChequeoAdmin)
admin.site.register(RitmoCardiaco)
admin.site.register(PresionSanguinea)
