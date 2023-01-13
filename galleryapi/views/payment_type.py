from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from galleryapi.models import PaymentType

class PaymentTypeView(ViewSet):
    '''The Gallery's Payment Type View'''
    
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
        
class PaymentTypeSerializer(serializers.ModelSerializer):
    '''JSON serializer for payment types'''
    class Meta:
        model = PaymentType
        fields = ('id', 'label', 'account_number', 'customer')
        depth = 1
