from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from app_api.models.product_size import ProductSize
from app_api.serializers.product_size_serializer import ProductSizeSerializer


class ProductSizeView(ViewSet):

    def list(self, request):
        product_size = ProductSize.objects.all()
        serializer = ProductSizeSerializer(product_size, many=True)
        return Response(serializer.data)

    