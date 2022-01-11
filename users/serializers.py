"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from users.models import User

# Email
from portal.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:

        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'other_first_name',
            'other_last_name',
            'id_type',
            'id_number',
            'profession',
            'profile',
        )


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer."""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # Phone number
    id_regex = RegexValidator(
        regex=r'\+?1?\d{8,10}$',
        message="La cedula debe ir en un formato numerico de la siguiente forma: +99999999. Hasta 10 caracteres permitidos."
    )
    id_type = serializers.ChoiceField(User.ID_TYPES)
    
    id_number = serializers.CharField(validators=[id_regex, UniqueValidator(queryset=User.objects.all())])

    # Password
    password = serializers.CharField(max_length=64)
    password_confirmation = serializers.CharField(max_length=64)

    # Name
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    other_first_name = serializers.CharField(max_length=30)
    other_last_name = serializers.CharField(max_length=30)
    
    profession = serializers.CharField(max_length=75)
    profile = serializers.CharField(max_length=300)

    def validate(self, data):
        """Verify passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Permite la creacion del usuario y envia el correo de bienvenida."""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        send_mail(
            'Bienvenido',
            'Bienvenido al Portal de Empleo.',
            EMAIL_HOST_USER,
            [data['email']],
            fail_silently=False,
        )
        return user

    

class UserLoginSerializer(serializers.Serializer):
    """User login serializer."""

    email = serializers.EmailField()
    password = serializers.CharField(max_length=64)

    def validate(self, data):
        """Comprobacion de credenciales."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Credenciales Incorrectas')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generacion de token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
