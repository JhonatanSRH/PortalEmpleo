"""Offers models."""

# Django
from django.db import models

# Models
from users.models import User

# Utils
from utils.models import BasePortalModel

class Offer(BasePortalModel, models.Model):
    """Offer Model."""
    
    offer_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    salary = models.FloatField()
    is_active = models.BooleanField(default=True)
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_id')
    updater_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updater_id')
    
class OfferApplication(BasePortalModel, models.Model):
    """Offer Application Model."""
    
    offer_application_id = models.AutoField(primary_key=True)
    applied_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applied_id')
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
