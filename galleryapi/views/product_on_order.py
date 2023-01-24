from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from galleryapi.models import ProductOnOrder
from .order import OrderSerializer

class ProductOnOrderView(ViewSet):
    """The Gallery's product on order view"""
    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """
        products_on_order = ProductOnOrder.objects.all()
        
        user_product_list = request.query_params.get('user', None)
        if user_product_list is not None:
            products_on_order = products_on_order.filter(user_id=user_product_list)
    # Product_on_order with an order_id of NULL are the list of products in the user's cart
        null_on_order = request.query_params.get('order', None)
        if null_on_order is not None:
            if null_on_order == "null":
                null_on_order = None
            else:
                null_on_order = "didn't work"
            products_on_order = products_on_order.filter(order_id=null_on_order)
        
        serializer = ProductOnOrderSerializer(products_on_order, many=True)
        return Response(serializer.data)
class ProductOnOrderSerializer(serializers.ModelSerializer):
    """JSON serializer for products on order"""
    class Meta:
        model = ProductOnOrder
        field = OrderSerializer(required=False, allow_null=True)
        fields = ('id', 'product', 'order', 'user')
        depth = 2
