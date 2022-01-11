"""Offer views."""

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

# Serializers
from offers.serializers import (
    OfferModelSerializer,
    OfferCreateSerializer,
    OfferApplicationModelSerializer,
    OfferApplicationRegisterSerializer
)

# Models
from offers.models import Offer, OfferApplication


class OfferView(APIView):
    """Offer View.
    Para registrar ofertas en la app"""
    
    def get(self, request):
        queryset = Offer.objects.all().order_by('-created')
        serializer = OfferModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        try:
            serializer = OfferCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            offer = serializer.save()
            data = OfferModelSerializer(offer).data
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        
class OfferApplicationView(APIView):
    """Offer Application View.
    Para postular usarios en ofertas"""
    
    def get(self, request):
        queryset = OfferApplication.objects.all().order_by('-created')
        serializer = OfferApplicationModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            serializer = OfferApplicationRegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            offer = serializer.save()
            data = OfferApplicationModelSerializer(offer).data
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)