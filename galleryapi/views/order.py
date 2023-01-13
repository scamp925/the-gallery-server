from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from galleryapi.models import Order

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
      
class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders"""
    class Meta:
        model = Order
        fields = ('id', 'total_cost', 'is_closed', 'customer', 'payment_type')
        depth = 1
