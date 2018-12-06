from django.db import models

# Create your models here.
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone


# modelos utilizados
class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    documento = models.DecimalField(default=0, max_length=5, decimal_places=0,
                                    max_digits=6)
    apellido = models.CharField(max_length=200)
    edad = models.DecimalField(default=0, max_length=5, decimal_places=0,
                               max_digits=3)


class Enfermero(Persona):
    piso = models.CharField(max_length=200)
    turno = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Paciente(Persona):
    sala = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class PacienteChequeo(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    enfermero = models.ForeignKey(Enfermero, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    presion_arterial = models.DecimalField(max_length=5, decimal_places=0,
                                           max_digits=3)
    ritmo_cardiaco = models.DecimalField(max_length=5, decimal_places=0,
                                         max_digits=3)

    observacion = models.CharField(max_length=200, null=True, default="")

    def __str__(self):
        return self.paciente.nombre + ' ' + self.paciente.apellido


@receiver(pre_save, sender=PacienteChequeo)
def pre_guardar(sender, instance, **kwargs):
    instance.fecha = timezone.now()


@receiver(post_save, sender=PacienteChequeo)
def post_guardar(sender, instance, **kwargs):
    if instance.presion_arterial > 0:
        print("Sigue vivo")
    if instance.ritmo_cardiaco > 10:
        print("La presion es normal")


class Rango(models.Model):
    diagnostico = models.CharField(max_length=10)
    min = models.DecimalField(max_length=5, decimal_places=0,
                              max_digits=3)
    max = models.DecimalField(max_length=5, decimal_places=0,
                              max_digits=3)


class RitmoCardiaco(Rango):
    def __str__(self):
        return self.diagnostico


class PresionSanguinea(Rango):
    def __str__(self):
        return self.diagnostico
