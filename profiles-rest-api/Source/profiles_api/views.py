# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializer

# Create your views here.
class HelloAPIView(APIView):
    """_summary_ : Testing Basic Hello World API View
    """
    serializer_class = serializer.HelloSerializers

    def get(self, request, format=None):
        """_summary_ : Return list of APIView features"""
        an_apiview = [
            'Uses HTTP method as functions (get, post, patch, put, detele)',
            'Is similar to tradition Django View',
            'Gives you most control over your application logic.',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello World', 'an_apiView':an_apiview})

    def post(self, request):
        """Create a hello message with out name"""
        serial = self.serializer_class(data=request.data)

        if serial.is_valid():
            name = serial.validated_data.get('name')
            return Response({'message':f'Hello, {name}'})
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle creating an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method':'DELETE'})
