from rest_framework import serializers

from .models import ADMIN, ConfirmationCode, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "bio",
            "email",
            "role",
        )

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        role = validated_data.get("role", None)
        instance = self.Meta.model(**validated_data)
        if role == ADMIN:
            instance.is_staff = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ConfirmationCodeSerializer(serializers.Serializer):
    class Meta:
        model = ConfirmationCode
        fields = ("email", "confirmation_code")
