from django.db.models import Q
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, UpdateAPIView, GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers.users import UserSerializer, UserAvatarSerializer, ChangePasswordValidator


class UsersListView(ListAPIView):
    serializer_class = UserSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email')

    def get_queryset(self):
        return User.objects.filter(is_active=True).order_by('id')


class UsersSearchView(APIView):
    def get(self, request, search):
        array = search.split(' ')

        if len(array) != 2:
            queryset = User.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
        else:
            queryset = User.objects.filter(
                Q(first_name__icontains=array[0]) | Q(last_name__icontains=array[0]) |
                Q(last_name__icontains=array[1]) | Q(first_name__icontains=array[1])
            )

        serializer = UserSerializer(queryset[:5], many=True)
        return Response({'results': serializer.data})


class UserSettingsView(UpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserAvatarSettingsView(UpdateAPIView):
    serializer_class = UserAvatarSerializer

    def get_object(self):
        return self.request.user


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordValidator

    def put(self, request):
        user = request.user
        data = ChangePasswordValidator.check(request.data, context={'request': request})

        user.set_password(data.get('new_password'))
        user.save()
        return Response(status=200)


class UserDetailView(APIView):
    def get(self, request, pk):
        instance = get_object_or_404(User, id=pk)
        data = UserSerializer(instance).data
        return Response(data)
