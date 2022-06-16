from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from app_api.models import UserPayment
from app_api.serializers import UserPaymentSerializer


class UserPaymentView(ViewSet):
   
    def list(self, request):
        """Get a list of payment types for the current user"""
        user_payments = UserPayment.objects.all()
        serializer = UserPaymentSerializer(user_payments, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a payment type for the current user"""
        try:
            user_payment = UserPayment.objects.create(
                user=request.auth.user,
                card_number=request.data['cardNumber'],
                exp_date=request.data['expDate'],

            )
            serializer = UserPaymentSerializer(user_payment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        """Delete a payment type"""
        try:
            user_payment = UserPayment.objects.get(pk=pk)
            user_payment.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except UserPayment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
