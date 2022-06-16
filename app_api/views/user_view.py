from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from app_api.serializers.user_serializer import UserSerializer


class UserView(ViewSet):

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        user = User.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
