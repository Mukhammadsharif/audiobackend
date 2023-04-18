from config import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from core.utils.serializers import ValidatorSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        if not obj.image:
            return None

        return settings.BACKEND_DOMAIN + obj.image.url

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'image',
            'expires_subscription_at',
            'date_joined'
        )
        extra_kwargs = {'image': {'read_only': True}}


class UserAvatarSerializer(ModelSerializer):
    def update(self, instance, data):
        super().update(instance, data)

        if not data.get('image'):
            instance.image = None

        return instance

    class Meta:
        model = User
        fields = ('id', 'image')


class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class ChangePasswordValidator(ValidatorSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)

    def validate_old_password(self, password):
        if not self.context['request'].user.check_password(password):
            raise ValidationError(_('Incorrect old password'))
        return password
