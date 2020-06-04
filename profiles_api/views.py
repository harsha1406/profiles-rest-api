#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer  #our module


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format= None):
        """Returns a list of APIView Features"""
        an_apiview = [
        'Uses HTTP methods as function(get, post, patch, put, delete)',
        'is similar to traditional Django view',
        'gives you the most control over logic',
        'is manually mapped to URLs'
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Creatr Hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating a object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
