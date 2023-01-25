from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from galleryapi.models import Product, ProductOnOrder, User
from .order import OrderSerializer

class ProductView(ViewSet):
    '''The Gallery's Product View'''

    def retrieve(self, request, pk):
        """Handle GET requests from single product
        Returns:
            Response -- JSON serialized product
        """
        try:
            product = Product.objects.get(pk=pk)

            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all products

        Returns:
            Response -- JSON serialized list of products
        """
        products = Product.objects.all()
            
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    @action(methods=['post'], detail=True)
    def add_to_cart(self, request, pk):
        """Post request to add user's product to the cart"""
        order = request.data['order_id']
        product = Product.objects.get(pk=pk)
        user = User.objects.get(pk=request.data['user'])
        ProductOnOrder.objects.create(
            order = order,
            product = product,
            user = user
        )
        return Response({'message': 'Product added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def remove_from_cart(self, request, pk):
        """Post request to add user's product to the cart"""
        product = Product.objects.get(pk=pk)
        user = User.objects.get(pk=request.data['user'])
        product_on_order = ProductOnOrder.objects.get(
            product = product,
            user = user
        )
        product_on_order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ProductSerializer(serializers.ModelSerializer):
    '''JSON serializer for products'''
    class Meta:
        model = Product
        field = OrderSerializer(required=False, allow_null=True)
        fields = ('id', 'title', 'description', 'image_url', 'price', 'quantity', 'seller')
        depth = 1
