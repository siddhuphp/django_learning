from rest_framework import serializers
from . models import players

class PlayersSerializers (serializers.ModelSerializer):
        
        class Meta:
            model = players
            # fields = ('first_name','last_name')
            fields = '__all__' 