#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format= None):
        """Returns a list of APIView Features"""
        an_apiview = [
        'Uses HTTP methods as function(get, post, patch, put, delete)',
        'is similar to traditional Django view',
        'gives you the most control over logic',
        'is manually mapped to URLs'
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})
