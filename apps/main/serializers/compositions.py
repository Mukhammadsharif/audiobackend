from rest_framework import serializers

from core.utils.serializers import ValidatorSerializer
from main.models import Composition, Liked, Deferred, Catalog
from main.serializers.authors import AuthorSerializer


class CompositionSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    is_deferred = serializers.SerializerMethodField()

    def get_is_liked(self, obj):
        return self.context['user'].is_authenticated \
               and Liked.objects.filter(composition=obj, user=self.context['user']).exists()

    def get_is_deferred(self, obj):
        return self.context['user'].is_authenticated \
               and Deferred.objects.filter(composition=obj, user=self.context['user']).exists()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = AuthorSerializer(instance.author).data
        return data

    class Meta:
        model = Composition
        fields = ("id", "title", "author", "genre", "subscription", "description", "audiobook_file", "image_file",
                  'size_of_audio', 'published_date', 'age_limit', 'is_liked', 'is_deferred', 'duration_of_audio',
                  )


class CompositionFilterSerializer(ValidatorSerializer):
    page = serializers.IntegerField(default=1)
    search = serializers.CharField(required=False)
    reverse = serializers.BooleanField(default=False)
    catalog = serializers.PrimaryKeyRelatedField(queryset=Catalog.objects.all(), required=False)
