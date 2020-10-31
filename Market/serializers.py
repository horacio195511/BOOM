from rest_framework import serializers
from Market.models import Thing


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = ['name', 'image', 'description', 'price']
