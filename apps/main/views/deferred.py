from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Deferred
from main.serializers.deferred import DeferredSerializer


class DeferredListView(APIView):
    def get(self, request):
        queryset = Deferred.objects.filter(user=request.user)
        serializer = DeferredSerializer(queryset, many=True, context={'user': request.user})
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = DeferredSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user, user=request.user)
        return Response(serializer.data, 201)


class DeferredDetailView(APIView):
    def delete(self, request, pk):
        instance = get_object_or_404(Deferred, user=request.user, composition_id=pk)
        instance.delete()
        return Response({}, 204)
