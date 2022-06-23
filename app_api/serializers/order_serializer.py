from rest_framework import serializers
from app_api.models import Order
from app_api.models.user_payment import UserPayment
from app_api.serializers.user_payment_serializer import UserPaymentSerializer


class OrderSerializer(serializers.ModelSerializer):
    user_payment = UserPaymentSerializer()
    class Meta:
        model = Order
        fields = ('id', 'product_size', 'address', 'created_on', 'completed_on', 'total', 'user_payment', 'date')
        depth = 4




class UpdateOrderSerializer(serializers.ModelSerializer):
    userPaymentId = serializers.IntegerField()

    class Meta:
        model = UserPayment
        fields = ('userPaymentId',)