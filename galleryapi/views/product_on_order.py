from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from galleryapi.models import ProductOnOrder, Product, Order

class ProductOnOrderView(ViewSet):
    """The Gallery's product on order view"""
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized product on order instance
        """
        product = Product.objects.get(pk=request.data['product_id'])
        # try:
        order = Order.objects.get(pk=request.data['order_id'])
        print(order, "What is this?")
        # except Order.DoesNotExist:
        #     order = None
        
        product_on_order = ProductOnOrder.objects.create(
            product=product,
            order=order
        )
        
        serializer = ProductOnOrderSerializer(product_on_order)
        return Response(serializer.data)

class ProductOnOrderSerializer(serializers.ModelSerializer):
    """JSON serializer for products on order"""
    model = ProductOnOrder
    fields = ('id', 'product', 'order')
    depth = 2
