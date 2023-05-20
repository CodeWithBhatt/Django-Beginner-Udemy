# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    """_summary_ : Testing Basic Hello World API View
    """

    def get(self, request, format=None):
        """_summary_ : Return list of APIView features"""
        an_apiview = [
            'Uses HTTP method as functions (get, post, patch, put, detele)',
            'Is similar to tradition Django View',
            'Gives you most control over your application logic.',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello World', 'an_apiView':an_apiview})
    
