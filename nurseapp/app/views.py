from django.http import JsonResponse
from rest_framework.views import APIView
from .models import PacienteChequeo, RitmoCardiaco, PresionSanguinea


class CharData(APIView):
    # endpoint para obtener los datos de un paciente
    def get(self, request, doc):
        pacientes = PacienteChequeo.objects.filter(paciente__documento=doc)
        labels = []
        data1 = []
        data2 = []
        for paciente in pacientes:
            labels.append(paciente.fecha)
            data1.append(paciente.ritmo_cardiaco)
            data2.append(paciente.presion_arterial)
        datos = {
            'labels': labels,
            'data1': data1,
            'data2': data2
        }
        return JsonResponse(datos)


class HeartRateEndPoint(APIView):
    # endpoint para diagnosticar el ritmo cardiaco
    def get(self, request, bpm):
        datos = {}
        for r in RitmoCardiaco.objects.all():
            if r.min <= bpm <= r.max:
                datos['status'] = 'Ritmo cardiaco es ' + r.diagnostico
        if not 'status' in datos:
            datos['status'] = 'Presión sanguínea PELIGROSA'
        return JsonResponse(datos)


class BloodPressureEndPoint(APIView):
    # endpoint para diagnosticar la presion sanguinea
    def get(self, request, press):
        datos = {}
        for r in PresionSanguinea.objects.all():
            if r.min <= press <= r.max:
                datos['status'] = 'Presión sanguínea es ' + r.diagnostico
        if not 'status' in datos:
            datos['status'] = 'Presión sanguínea PELIGROSA'
        return JsonResponse(datos)
