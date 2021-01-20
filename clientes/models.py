from django.db import models

# Create your models here.
class Cliente(models.Model):
    ESPECIAL = 'ES'
    POTENCIAL = 'PO'
    NORMAL = 'NO'
    INACTIVO = 'IN'

    STATUS = (
        (ESPECIAL, 'Especial'),
        (POTENCIAL, 'Potencial'),
        (NORMAL, 'Normal'),
        (INACTIVO, 'Inactivo'),
    )
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    edad = models.IntegerField(verbose_name="Edad")
    status = models.CharField(choices=STATUS, default=NORMAL, max_length=2, verbose_name="Status")
    dni = models.CharField(verbose_name="DNI", max_length=11, unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        

    def __str__(self):
        return self.nombre
