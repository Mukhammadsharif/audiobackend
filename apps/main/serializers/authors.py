from rest_framework import serializers

from core.utils.serializers import ValidatorSerializer
from main.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'full_name', 'username', 'email', 'phone')


class AuthorFilterSerializer(ValidatorSerializer):
    page = serializers.IntegerField(default=1)
