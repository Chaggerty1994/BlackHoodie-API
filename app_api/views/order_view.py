from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from app_api.models import Order, UserPayment

from app_api.serializers import OrderSerializer



class OrderView(ViewSet):

   
    def list(self, request):
        """Get a list of the current users orders
        """
        orders = Order.objects.filter(user=request.auth.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    
    def destroy(self, request, pk):
        """Delete an order, current user must be associated with the order to be deleted
        """
        try:
            order = Order.objects.get(pk=pk, user=request.auth.user)
            order.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['post'], detail=False)
    def complete(self, request):
        """Complete an order by adding a payment type and completed data
        """
        try:
            order = Order.objects.create( user=request.auth.user)
            order.products.add(*request.data["products"])
            address=request.data["address"]
            user_payment = UserPayment.objects.get(
                pk=request.data['userPaymentId'], user=request.auth.user)
            order.user_payment = user_payment
            order.address = address
            order.completed_on = datetime.now()
            order.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except (Order.DoesNotExist, UserPayment.DoesNotExist) as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    
    @action(methods=['get'], detail=False)
    def current(self, request):
        """Get the user's current order"""
        try:
            order = Order.objects.get(
                completed_on=None, user=request.auth.user)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({
                'message': 'You do not have an open order. Add a product to the cart to get started'},
                status=status.HTTP_404_NOT_FOUND
            )
