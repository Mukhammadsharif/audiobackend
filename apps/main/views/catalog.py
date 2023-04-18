from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils.pagination import pagination
from main.models import Author, Catalog
from main.serializers.catalog import CatalogSerializer, CatalogFilterSerializer


class CatalogListView(APIView):
    def get(self, request):
        params = CatalogFilterSerializer.check(request.GET)
        query = Catalog.objects.all()
        serializer = CatalogSerializer(query, many=True)
        data = pagination(query, serializer, params.get('page'), 100)
        return Response(data)


class CatalogDetailView(APIView):
    def get(self, request, pk):
        instance = get_object_or_404(Author, id=pk)
        data = CatalogSerializer(instance).data
        return Response(data)
