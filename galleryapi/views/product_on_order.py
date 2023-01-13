from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from galleryapi.models import ProductOnOrder, Product, Order

class ProductOnOrderView(ViewSet):
    """The Gallery's product on order view"""
    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """
        products_on_order = ProductOnOrder.objects.all()
    
        serializer = ProductOnOrderSerializer(products_on_order, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized product on order instance
        """
        product = Product.objects.get(pk=request.data['product_id'])
        order = Order.objects.get(pk=request.data['order_id'])
        
        product_on_order = ProductOnOrder.objects.create(
            product=product,
            order=order
        )
        
        serializer = ProductOnOrderSerializer(product_on_order)
        return Response(serializer.data)

    def destroy(self, request, pk):
        products = ProductOnOrder.objects.get(pk=pk)
        products.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class ProductOnOrderSerializer(serializers.ModelSerializer):
    """JSON serializer for products on order"""
    class Meta:
        model = ProductOnOrder
        fields = ('id', 'product', 'order')
        depth = 2
