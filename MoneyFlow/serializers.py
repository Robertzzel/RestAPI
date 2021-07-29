from rest_framework import serializers
from .models import Produs


class ProdusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produs
        fields = ('nume','pret','data')

class AdaugaProdusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produs
        fileds = ('nume','pret','data')