from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils.pagination import pagination
from main.models import Author, Composition
from main.serializers.compositions import CompositionSerializer, CompositionFilterSerializer


class CompositionListView(APIView):
    def get(self, request):
        params = CompositionFilterSerializer.check(request.GET)
        query = Composition.objects.list(
            search=params.get("search"),
            reverse=params.get('reverse'),
            catalog=params.get('catalog')
        )
        serializer = CompositionSerializer(query, many=True, context={'user': request.user})
        data = pagination(query, serializer, params.get('page'), 100)
        return Response(data)

    def post(self, request):
        serializer = CompositionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, 201)


class CompositionDetailView(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Composition, id=pk)
        serializer = CompositionSerializer(queryset, context={'user': request.user})
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = get_object_or_404(Composition, id=pk, user=request.user)
        instance.delete()
        return Response({}, 204)

    def put(self, request, pk):
        instance = get_object_or_404(Author, id=pk)
        serializer = CompositionSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=request.user)
        return Response(serializer.data)
