from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenBlacklistSerializer

from app.users.api.serializers import (
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer,
    UserUpdateSerializer,
)

User = get_user_model()


class UserView(ListCreateAPIView):
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.all().order_by("-id")

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs["user_id"]
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {
                    "message": "Not Found",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data
        serializer = UserUpdateSerializer(user, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()


class TokenLogoutView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        token = request.auth.token
        token_refresh = token.decode("utf-8")
        serializer = TokenBlacklistSerializer(data={"refresh": token_refresh})
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
