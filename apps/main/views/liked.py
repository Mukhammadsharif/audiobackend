from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Liked

from main.serializers.liked import LikedSerializer


class LikedListView(APIView):
    def get(self, request):
        queryset = Liked.objects.filter(user=request.user)
        serializer = LikedSerializer(queryset, many=True, context={'user': request.user})
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = LikedSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user, user=request.user)
        return Response(serializer.data, 201)


class LikedDetailView(APIView):
    def delete(self, request, pk):
        instance = get_object_or_404(Liked, user=request.user, composition_id=pk)
        instance.delete()
        return Response({}, 204)
