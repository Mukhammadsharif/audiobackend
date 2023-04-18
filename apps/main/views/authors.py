from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils.pagination import pagination
from main.models import Author
from main.serializers.authors import AuthorFilterSerializer, AuthorSerializer


class AuthorListView(APIView):
    def get(self, request):
        params = AuthorFilterSerializer.check(request.GET)
        query = Author.objects.all()
        serializer = AuthorSerializer(query, many=True)
        data = pagination(query, serializer, params.get('page'), 100)
        return Response(data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, 201)


class AuthorDetailView(APIView):
    def get(self, request, pk):
        instance = get_object_or_404(Author, id=pk)
        data = AuthorSerializer(instance).data
        return Response(data)

    def delete(self, request, pk):
        instance = get_object_or_404(Author, id=pk, user=request.user)
        instance.delete()
        return Response({}, 204)

    def put(self, request, pk):
        instance = get_object_or_404(Author, id=pk)
        serializer = AuthorSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=request.user)
        return Response(serializer.data)
