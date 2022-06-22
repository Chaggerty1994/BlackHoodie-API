from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from app_api.models import Product, Order
from app_api.serializers import ProductSerializer
from app_api.serializers.order_serializer import UpdateOrderSerializer
from rest_framework.permissions import AllowAny

from app_api.serializers.product_serializer import UpdateProductSerializer

class ProductView(ViewSet):
    permission_classes = [AllowAny]
    def list(self, request):
        """Get a list of all products"""
        products = Product.objects.all()
        category = request.query_params.get('category', None)
        name = request.query_params.get('name', None)

        if category is not None:
            products = products.filter(category__id=category)

        if name is not None:
            products = products.filter(name__icontains=name)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Get a single product"""
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
  
        product = Product.objects.get(pk=pk)
        serializer = UpdateProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


    @action(methods=['post'], detail=True)
    def add_to_order(self, request, pk):
        """Add a product to the current users open order"""
        try:
            product = Product.objects.get(pk=pk)
            order, _ = Order.objects.get_or_create(
                user=request.auth.user, completed_on=None, payment_type=None)
            order.products.add(product)
            return Response({'message': 'product added'}, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['delete'], detail=True)
    def remove_from_order(self, request, pk):
        """Remove a product from the users open order"""
        try:
            product = Product.objects.get(pk=pk)
            order = Order.objects.get(
                user=request.auth.user, completed_on=None)
            order.product.remove(product)
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except (Product.DoesNotExist, Order.DoesNotExist) as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
