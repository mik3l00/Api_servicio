from django.urls import path, include
from rest_framework import routers
from api import views
 
router = routers.DefaultRouter()
router.register(r'tipo_cotizacion_riego', views.tipo_cotizacion_riegoViewSet)
 
urlpatterns = [
    path('', include(router.urls)),
]