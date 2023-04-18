from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from main.models import Deferred
from main.serializers.compositions import CompositionSerializer


class DeferredSerializer(serializers.ModelSerializer):
    def validate_composition(self, composition):
        if Deferred.objects.filter(user=self.context.get('user'), composition=composition).exists():
            raise ValidationError({'composition': _('The composition is already deferred')})

        return composition

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['composition'] = CompositionSerializer(instance.composition, context={'user': self.context.get('user')}).data
        return data

    class Meta:
        model = Deferred
        fields = ('id', 'composition')
