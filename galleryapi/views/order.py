from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from galleryapi.models import Order, User, PaymentType

class OrderView(ViewSet):
    '''The Gallery's Order View'''
    
    def list(self, request):
        """Handle GET requests to get all closed orders

        Returns:
            Response -- JSON serialized list of orders
        """
        orders = Order.objects.all()
        
        # endpoint: {{dbUrl}}/orders?closed=true => renders all closed orders
        closed_orders = request.query_params.get('closed', None)
        if closed_orders is not None:
            orders = orders.filter(is_closed=True)
            
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized order instance
        """
        customer = User.objects.get(uid=request.data['customer_id'])
        payment_type = PaymentType.objects.get(pk=request.data['payment_type_id'])
        
        order = Order.objects.create(
            total_cost=request.data['total_cost'],
            is_closed=True,
            customer=customer,
            payment_type=payment_type
        )
        
        serializer = OrderSerializer(order)
        return Response(serializer.data)
      
class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders"""
    class Meta:
        model = Order
        fields = ('id', 'total_cost', 'is_closed', 'customer', 'payment_type')
        depth = 1
