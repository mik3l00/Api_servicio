from django.contrib import admin
from .models import tipo_cotizacion_riego,tipo_cotizacion_electrico, servicio_riego,servicio_electrico,productos, medida_producto

@admin.register(tipo_cotizacion_riego)
class tipo_cotizacion_riegoAdmin(admin.ModelAdmin):
    list_display = ('tipo_servicio',)

@admin.register(tipo_cotizacion_electrico)
class tipo_cotizacion_electricoAdmin(admin.ModelAdmin):
    list_display = ('tipo_servicio',)
    
@admin.register(servicio_riego)
class servicio_riegoAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'detalle_servicio', 'valor_servicio')

@admin.register(servicio_electrico)
class servicio_electricoAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'detalle_servicio', 'valor_servicio')

@admin.register(productos)
class productosAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio_producto', 'cantidad_producto', 'id_cotizacion')

@admin.register(medida_producto)
class medida_productoAdmin(admin.ModelAdmin):
    list_display = ('medida', 'costo', 'id_productos')