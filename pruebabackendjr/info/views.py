#from django.http import response
from django.shortcuts import render

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from info.serializers import EstadoSerializer, MunicipioSerializer, ColoniaSerializer

from info.models import Estado, Municipio, Colonia

class estado(APIView):
    def get(self, request):
        try:
           estados = Estado.objects.all().values()
           return Response(estados, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
    

class estado_nombre(APIView):
    def get(self, request, nombre):
        try:
           estado= Estado.objects.filter(d_estado=nombre).first()
           municipio= Municipio.objects.filter(estado=estado.id)
           serializer_estado = EstadoSerializer(estado)
           #print(serializer_estado(municipio).data)
           return Response(serializer_estado.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class municipio(APIView):
    def get(self, request):
        try:
           municipios = Municipio.objects.all().values()
           return Response(municipios, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class municipio_nombre(APIView):
    def get(self, request, nombre):
        try:
           municipio= Municipio.objects.filter(D_mnpio=nombre).first()
           serializer_municipio = MunicipioSerializer(municipio)
           #print(serializer_estado(municipio).data)
           return Response(serializer_municipio.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class colonia(APIView):
    def get(self, request):
        try:
           colonias = Colonia.objects.all().values()
           return Response(colonias, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class colonia_nombre(APIView):
    def get(self, request, nombre):
        try:
           colonia= Colonia.objects.filter(d_asenta=nombre).first()
           serializers_colonia = ColoniaSerializer(colonia)
           return Response(serializers_colonia.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class colonia_cp(APIView):
    def get(self, request, cp):
        try:
           colonia= Colonia.objects.filter(d_CP=cp).all()
           serializers_colonia = ColoniaSerializer(colonia)
           return Response(serializers_colonia.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
    