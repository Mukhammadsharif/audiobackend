from rest_framework import serializers

from core.utils.serializers import ValidatorSerializer
from main.models import Catalog


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('id', 'title', 'image',)


class CatalogFilterSerializer(ValidatorSerializer):
    page = serializers.IntegerField(default=1)
