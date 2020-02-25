from django.shortcuts import render
from . models import fruits,Album
from rest_framework import viewsets
from . serializers import FruitsSerializers

class FruitsView(viewsets.ModelViewSet):

      queryset = fruits.objects.all()
      serializer_class = FruitsSerializers

      queryset = Album.objects.all()
      serializer_class = FruitsSerializers


