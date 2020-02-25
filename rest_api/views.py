from django.shortcuts import render
from rest_framework import viewsets
from . serializers import PlayersSerializers
from . models import players

class PlayerView(viewsets.ModelViewSet):
    queryset = players.objects.all()
    serializer_class = PlayersSerializers

# Create your views here.

