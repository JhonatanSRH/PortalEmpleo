"""Offers serializers."""

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator, ValidationError

# Serializers
from users.serializers import UserModelSerializer

# Models
from users.models import User
from offers.models import Offer, OfferApplication


class OfferModelSerializer(serializers.ModelSerializer):
    """Offer model serializer."""

    creator_id = UserModelSerializer(read_only=True)
    updater_id = UserModelSerializer(read_only=True)
    
    class Meta:

        model = Offer
        fields = (
            'offer_id',
            'title',
            'description',
            'salary',
            'is_active',
            'creator_id',
            'updater_id',
        )
        
class OfferCreateSerializer(serializers.Serializer):
    """Offer create serializer."""

    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=500)
    salary = serializers.FloatField()
    creator_id = serializers.IntegerField()
    
    def validate(self, data):
        """Verifica si el creador existe."""
        User.objects.get(id=data['creator_id'])
        return data
    
    def create(self, data):
        """Crea la oferta."""
        data['creator_id'] = User.objects.get(id=data['creator_id'])
        data['updater_id'] = data['creator_id']
        offer = Offer.objects.create(**data)
        return offer
    
class OfferApplicationModelSerializer(serializers.ModelSerializer):
    """Offer model serializer."""

    applied_id = UserModelSerializer(read_only=True)
    offer = OfferModelSerializer(read_only=True)
    
    class Meta:

        model = OfferApplication
        fields = '__all__'

class OfferApplicationRegisterSerializer(serializers.Serializer):
    """Offer model serializer."""

    applied_id = serializers.IntegerField()
    offer = serializers.IntegerField()
    
    def validate(self, data):
        """Verifica si el creador existe y la oferta existe."""
        User.objects.get(id=data['applied_id'])
        Offer.objects.get(offer_id=data['offer'])
        return data
    
    def create(self, data):
        """Crea la postulacion de la oferta."""
        data['applied_id'] = User.objects.get(id=data['applied_id'])
        data['offer'] = Offer.objects.get(offer_id=data['offer'])
        if OfferApplication.objects.filter(**data).count() != 0:
            raise ValidationError('Ya se ha hecho la postulacion anteriormente')
        offer_application = OfferApplication.objects.create(**data)
        return offer_application