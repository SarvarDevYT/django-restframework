from django.shortcuts import render
from rest_framework import generics
from .models import Talaba, Avtomobil
from .serializers import TalabaSerializers, AvtomobilSerializer

class MalumotAPi(generics.ListAPIView):
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializers

class AvtomobilListCreateAPI(generics.ListCreateAPIView):
    queryset = Avtomobil.objects.all()
    serializer_class = AvtomobilSerializer
