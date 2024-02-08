from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import tipo_cotizacion_riego
from .serializer import tipo_cotizacion_riegoSerializer
from rest_framework import status

def login(request):
   c={
       'titulo':'hola',
       'mensaje':'como estas',
       'api':'ya estoy conectado',   
   }

   template ='inicio.html'
   return render(request,template,c)

@api_view()
def inicio(request):
    return Response({"message": "Hello, world!"})



# Create your views here.
 
class tipo_cotizacion_riegoViewSet(viewsets.ModelViewSet):
    queryset = tipo_cotizacion_riego.objects.all()
    serializer_class= tipo_cotizacion_riegoSerializer