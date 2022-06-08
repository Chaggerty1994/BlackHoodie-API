from unicodedata import category
from rest_framework import serializers

from app_api.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        depth = 1
