#from django.http import response
from django.shortcuts import render

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from info.serializers import EstadoSerializer, MunicipioSerializer, ColoniaSerializer

from info.models import Estado, Municipio, Colonia

def index(request):
	return render(request,'index.html')

class estado(APIView):
    def get(self, request):
        try:
            estado_nombre = request.GET.get("nombre")
            if estado_nombre is None or estado_nombre=='':
                estados = Estado.objects.all().values()
                return render(request, 'estado.html', {'estados': estados})
            else:
                estados= Estado.objects.filter(d_estado=estado_nombre).values()
                #estados = EstadoSerializer(estado)
                return render(request, 'estado.html', {'estados': estados})           
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
    



class municipio(APIView):
    def get(self, request):
        try:
            municipio_nombre = request.GET.get("nombre")
            if municipio_nombre is None or municipio_nombre=='':
                municipios = Municipio.objects.all().values()
                return render(request, 'municipio.html')
            else:
                municipios= Municipio.objects.filter(D_mnpio=municipio_nombre).values()
                municipio= Municipio.objects.filter(D_mnpio=municipio_nombre).first()
                #estados = EstadoSerializer(estado)
                return render(request, 'municipio.html', {'municipios': municipios, 'estados': municipio.estado})           
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class colonia(APIView):
    def get(self, request):
        try:
            colonia_nombre = request.GET.get("nombre")
            if colonia_nombre is None or colonia_nombre=='':
                colonias = Colonia.objects.all().values()
                return render(request, 'colonia.html')
            else:
               
                data = {}
                data['colonia'] = Colonia.objects.filter(d_asenta=colonia_nombre).values()
                data['municipio'] = Municipio.objects.all()
                return render(request, 'colonia.html', data)           
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class colonia_cp(APIView):
    def get(self, request, cp):
        try:
           colonia= Colonia.objects.filter(d_CP=cp).all()
           serializers_colonia = ColoniaSerializer(colonia, many=True)
           return Response(serializers_colonia.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
    