from rest_framework import serializers
from main.models import Images


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
