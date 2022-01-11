"""Users views."""

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny

# Serializers
from users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)

# Models
from users.models import User


class UserSignUpView(APIView):
    """User View.
    Para registrar usuarios en la app"""
    
    permission_classes = [AllowAny]
    
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        try:
            serializer = UserSignUpSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            data = UserModelSerializer(user).data
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        
class UserLoginView(APIView):
    """User Login View.
    Para loguear usuarios en la app"""
    
    permission_classes = [AllowAny]
        
    def post(self, request):
        """login."""
        try:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user, token = serializer.save()
            data = {
                'user': UserModelSerializer(user).data,
                'access_token': token
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)