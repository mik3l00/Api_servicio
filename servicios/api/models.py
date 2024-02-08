from django.db import models


#Crear modelo de Base de datos


class tipo_cotizacion_riego(models.Model):
    tipo_servicio = models.CharField(max_length=144)
    def __str__(self) -> str:
        return f"{self.tipo_servicio}"

class tipo_cotizacion_electrico(models.Model):
    tipo_servicio = models.CharField(max_length=144)

    def __str__(self) -> str:
        return f"{self.tipo_servicio}"

class servicio_riego(models.Model):
    nombre_servicio = models.ForeignKey(tipo_cotizacion_riego, related_name='servicios_riego', on_delete=models.SET_NULL, null=True)
    detalle_servicio = models.TextField(max_length=400)
    valor_servicio = models.DecimalField(max_digits=10, decimal_places=2)

class servicio_electrico(models.Model):
    nombre_servicio = models.ForeignKey(tipo_cotizacion_electrico, related_name='servicios_electrico', on_delete=models.SET_NULL, null=True)
    detalle_servicio = models.TextField(max_length=400)
    valor_servicio = models.DecimalField(max_digits=10, decimal_places=2)

IVA_CHOICES = (
    ("0", "12"),
    ("1", "0"),
)

class productos(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_producto = models.IntegerField()
    #imagen_producto
    iva = models.CharField(max_length=6, choices=IVA_CHOICES, default= False)
    id_cotizacion = models.ForeignKey(tipo_cotizacion_riego, related_name='productos', on_delete=models.SET_NULL, null=True)

class medida_producto(models.Model):
    medida = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    id_productos = models.ForeignKey(productos, related_name='medida_producto', on_delete=models.SET_NULL, null=True)




    def __str__(self) -> str:
        return f"{self.tipo_servicio}"