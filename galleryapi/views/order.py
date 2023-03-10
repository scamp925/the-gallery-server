from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from galleryapi.models import Order, User, PaymentType, ProductOnOrder, Product

class OrderView(ViewSet):
    '''The Gallery's Order View'''
    
    def list(self, request):
        """Handle GET requests to get all closed orders

        Returns:
            Response -- JSON serialized list of orders
        """
        orders = Order.objects.all()
        
        # endpoint: {{dbUrl}}/orders?user=${customer_id}&closed=true => renders all closed orders
        # endpoint: {{dbUrl}}/orders?user=${customer_id}&closed=false => renders all open orders
        user = request.query_params.get('user', None)
        if user is not None:
            orders = orders.filter(customer_id=user)
            
        closed_orders = request.query_params.get('closed', None)
        if closed_orders is not None:
            if closed_orders == "true":
            
                closed_orders = True
            else:
                closed_orders = False
            
            orders = orders.filter(is_closed=closed_orders)
        
        # Response -- A list of all products associated with a specific order
        for order in orders:
            filtered_products_on_order = ProductOnOrder.objects.filter(order=order.id)
            associated_products = []
            
            for product_on_order_obj in filtered_products_on_order:
                # Making a product dictionary to be able to in the frontend get the individual values and display them properly. Will append to associated_products making it an array of objects for the FE
                product_dict={}
                try:
                    products_on_order = Product.objects.get(id=product_on_order_obj.product_id)
                    product_dict['id']=products_on_order.id
                    product_dict['title']=products_on_order.title
                    product_dict['image_url']=products_on_order.image_url
                except:
                    pass
                
                # Still in the loop, finding the seller of the product for each product on an order 
                seller_info = User.objects.get(id=products_on_order.seller.id)
                product_dict['first_name']=seller_info.first_name
                product_dict['last_name']=seller_info.last_name
            
                associated_products.append(product_dict)
                        
            order.associated_products = associated_products
            
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized order instance
        """
        customer = User.objects.get(pk=request.data['customer_id'])
        payment_type = PaymentType.objects.get(pk=request.data['payment_type_id'])
        
        order = Order.objects.create(
            total_cost=request.data['total_cost'],
            is_closed=True,
            customer=customer,
            payment_type=payment_type
        )
        
        associated_product_ids = request.data['associated_product_ids']
        
        products = [Product.objects.get(pk=product_id) for product_id in associated_product_ids]
        
        for product in products:
            product_on_order = ProductOnOrder(product=product, order=order)
            product_on_order.save()
            
        serializer = OrderSerializer(order)
        return Response(serializer.data)
      
class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders"""
    class Meta:
        model = Order
        fields = ('id', 'total_cost', 'is_closed', 'customer', 'payment_type', 'associated_products')
        depth = 1
