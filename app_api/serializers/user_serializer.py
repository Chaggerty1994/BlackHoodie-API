from rest_framework import serializers
from django.contrib.auth.models import User

from app_api.serializers.order_serializer import OrderSerializer






class UserSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'orders')
        depth = 2


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
