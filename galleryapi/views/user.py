from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from galleryapi.models import User

class UserView(ViewSet):
    '''The Gallery User View'''
    def retrieve(self, request, pk):
        user = User.objects.get(pk=pk)
        
        serializer = UserSerializer(user)
        
        return Response(serializer.data)
      
    def list(self, request):
        """Handle GET requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
       
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'profile_image_url', 'created_on', 'is_seller', 'uid')
