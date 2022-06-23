from rest_framework import serializers

from app_api.models.product_size import ProductSize


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ('id', 'product', 'size')
        depth = 2