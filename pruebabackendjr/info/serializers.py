from info.models import Estado, Municipio, Colonia
from rest_framework import serializers


class ColoniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colonia
        fields = ['d_asenta', 'd_tipo_asenta', 'd_CP', 'municipio']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['D_mnpio', 'estado']

class EstadoSerializer(serializers.ModelSerializer):
    #municipio = MunicipioSerializer(many=True)
    class Meta:
        model = Estado
        fields = ['d_estado']


