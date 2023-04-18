from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext_lazy as _

from core.utils.serializers import ValidatorSerializer
from users.models import User
from datetime import datetime

from users.utils.emails import send_verification_email


class SignUpSerializer(serializers.ModelSerializer):
    is_mobile = serializers.BooleanField(write_only=True, default=False)

    def validate_email(self, email):
        User.objects.remove_unverified(email.lower())
        return email.lower()

    def create(self, data):
        data['email'] = data['email'].lower()
        data['username'] = data['email']  # Use email as username
        is_mobile = data.pop('is_mobile')
        user = User.objects.create_user(**data, is_active=True, expires_subscription_at=datetime.now())
        send_verification_email(self.context.get('request'), user, is_mobile)
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'is_mobile')
        extra_kwargs = {
            'email': {'required': True, 'validators': [UniqueValidator(
                queryset=User.objects.unique_query(),
                message=_("User with this email already exists.")
            )]},
            'first_name': {'required': True},
            'invitation_token': {'required': False},
            'last_name': {'required': True},
            'password': {'write_only': True},
        }


class ConfirmationValidator(ValidatorSerializer):
    confirmation_code = serializers.CharField(required=True)
