"""Users urls."""

# Django
from django.urls import path

# Views
from users.views import UserSignUpView, UserLoginView

# Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserSignUpView.as_view(), basename='users')

urlpatterns = [
    path('api/user/signup', UserSignUpView.as_view(), name='signup'),
    path('api/user/login', UserLoginView.as_view())
]

