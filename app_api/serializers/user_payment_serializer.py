from rest_framework import serializers
from app_api.models import UserPayment

class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = ('id', 'obscured_num', 'exp_date',  'user')

class CreatePaymentType(serializers.Serializer):
    card_number = serializers.CharField()
    exp_date = serializers.CharField()
