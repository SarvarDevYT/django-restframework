from rest_framework import serializers
from .models import Talaba, Avtomobil

class TalabaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'

class AvtomobilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avtomobil
        fields = '__all__'
