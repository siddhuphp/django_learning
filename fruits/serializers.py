from rest_framework import serializers
from . models import fruits,Album

class FruitsSerializers (serializers.ModelSerializer):
        
        class Meta:
            model = fruits
            # fields = ('first_name','last_name')
            fields = '__all__' 

        class Meta:
            model = Album
            # fields = ('first_name','last_name')
            fields = '__all__'