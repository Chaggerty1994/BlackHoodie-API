from rest_framework import serializers
from app_api.models import Size


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'size')
        depth = 1