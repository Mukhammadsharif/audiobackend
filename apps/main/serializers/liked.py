from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from main.models import Liked
from rest_framework.exceptions import ValidationError

from main.serializers.compositions import CompositionSerializer


class LikedSerializer(serializers.ModelSerializer):
    def validate_composition(self, composition):
        if Liked.objects.filter(user=self.context.get('user'), composition=composition).exists():
            raise ValidationError({'composition': _('The composition is already liked')})

        return composition

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['composition'] = CompositionSerializer(instance.composition, context={'user': self.context.get('user')}).data
        return data

    class Meta:
        model = Liked
        fields = ('id', 'composition')
