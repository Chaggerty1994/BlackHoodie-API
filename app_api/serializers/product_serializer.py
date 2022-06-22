from rest_framework import serializers
from app_api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'category', 'image_path')
        depth = 2

class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('size',)
    

class CreateProductSerializer(serializers.Serializer):
    categoryId = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=7)
    image = serializers.ImageField()






