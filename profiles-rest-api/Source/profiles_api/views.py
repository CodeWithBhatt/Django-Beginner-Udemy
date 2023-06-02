# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializer, models, permissions

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
        return Response({'message':'Hello API View', 'an_apiView':an_apiview})

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

class HelloViewSet(viewsets.ViewSet):
    """_summary_ : Test API View Set
    """
    serializer_class = serializer.HelloSerializers
    
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "Uses actions (list, create, retrive, update, partial update)",
            'Automatically maps to URLs using router',
            "provides more functionality with less codes"
        ]
        return Response({"message":"Hello View Set", "a_viewset":a_viewset})

    def create(self, request):
        """Create a hello message with out name"""
        serial = self.serializer_class(data=request.data)

        if serial.is_valid():
            name = serial.validated_data.get('name')
            return Response({'message':f'Hello, {name}'})
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializer.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user Authentication Token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES