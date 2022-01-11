"""Offers urls."""

# Django
from django.urls import path

# Views
from offers.views import OfferView, OfferApplicationView

# Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'offers', OfferView.as_view(), basename='offers')
router.register(r'offers', OfferApplicationView.as_view(), basename='offers')

urlpatterns = [
    path('api/offers', OfferView.as_view()),
    path('api/offers/apply', OfferApplicationView.as_view()),
]