from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app_api import serializers
from app_api.models import Size
from app_api.serializers import SizeSerializer
from rest_framework.permissions import AllowAny

class SizeView(ViewSet):
    permission_classes = [AllowAny]
    def list(self, request):
        """Get a list of categories
        """
        sizes = Size.objects.all()
        serializer = SizeSerializer(sizes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        size = Size.get(pk=pk)
        serializer = SizeSerializer(size)
        return Response(serializer.data)
        