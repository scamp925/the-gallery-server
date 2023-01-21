from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from galleryapi.models import PaymentType, User

class PaymentTypeView(ViewSet):
    '''The Gallery's payment type view'''
    
    def retrieve(self, request, pk):
        """Handle GET requests from single payment type
        Returns:
            Response -- JSON serialized payment type
        """
        try:
            payment_type = PaymentType.objects.get(pk=pk)

            serializer = PaymentTypeSerializer(payment_type)
            return Response(serializer.data)
        except PaymentType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """Handle GET requests to get all payment types

        Returns:
            Response -- JSON serialized list of payment types
        """
        payment_types = PaymentType.objects.all()
        
        # endpoint: {{dbUrl}}/paymenttypes?user=1 => shows all associated payment types of a single user
        payment_types_of_user = request.query_params.get('user', None)
        if payment_types_of_user is not None:
            payment_types = payment_types.filter(customer_id=payment_types_of_user)
            
        serializer = PaymentTypeSerializer(payment_types, many=True)
        
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized payment type instance
        """
        customer = User.objects.get(pk=request.data['customer_id'])
        
        payment_type = PaymentType.objects.create(
            label=request.data['label'],
            account_number=request.data['account_number'],
            customer=customer
        )
        
        serializer = PaymentTypeSerializer(payment_type)
        return Response(serializer.data)
      
    def update(self, request, pk):
        """Handle PUT requests for a payment type

        Returns:
            Response -- Empty body with 204 status code
        """
        
        payment_type = PaymentType.objects.get(pk=pk)
        payment_type.label = request.data['label']
        payment_type.account_number = request.data['account_number']
        
        payment_type.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        payment_type = PaymentType.objects.get(pk=pk)
        payment_type.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class PaymentTypeSerializer(serializers.ModelSerializer):
    '''JSON serializer for payment types'''
    class Meta:
        model = PaymentType
        fields = ('id', 'label', 'account_number', 'customer')
        depth = 1
