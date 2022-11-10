from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone", "avatar", "fullname"]


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, max_length=255)
    password = serializers.CharField(
        required=True, max_length=128, write_only=True
    )
    phone = serializers.CharField(required=True, max_length=15)
    first_name = serializers.CharField(
        required=False, allow_null=True, allow_blank=True, max_length=150
    )
    last_name = serializers.CharField(
        required=False, allow_null=True, allow_blank=True, max_length=150
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "phone",
            "password",
            "avatar",
            "first_name",
            "last_name",
        ]

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone", "avatar", "fullname"]


class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False, allow_null=True, allow_blank=True, max_length=255
    )
    phone = serializers.CharField(
        required=False, allow_null=True, allow_blank=True, max_length=15
    )
    first_name = serializers.CharField(
        required=False, allow_null=True, allow_blank=True, max_length=150
    )
    last_name = serializers.CharField(
        required=False, allow_null=True, allow_blank=True, max_length=150
    )

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        if email := validated_data.get("email"):
            instance.email = email
        if phone := validated_data.get("phone"):
            instance.phone = phone
        if first_name := validated_data.get("first_name"):
            instance.first_name = first_name
        if last_name := validated_data.get("last_name"):
            instance.last_name = last_name
        instance.save()


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
