from rest_framework import serializers
from .models import CategorySigns,RoadSigns


class CategorSignsSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    class Meta:
        model=CategorySigns
        fields='__all__'

class RoadSignsSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    category=serializers.CharField(max_length=100)
    image=serializers.ImageField()
    video=serializers.FileField()
    audio=serializers.FileField()
    dock=serializers.FileField()
    
    class Meta:
        model=RoadSigns
        fields='__all__'