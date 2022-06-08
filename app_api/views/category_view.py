from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app_api import serializers
from app_api.models import Category
from app_api.serializers import CategorySerializer


class CategoryView(ViewSet):

    def list(self, request):
        """Get a list of categories
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        category = Category.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
        