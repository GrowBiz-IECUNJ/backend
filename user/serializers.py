from rest_framework import serializers
from .models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = [
            "email",
            "name",
            "password",
            "password2",
            "phone",
            "birth_date",
            "address",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        user = MyUser(
            email=self.validated_data["email"],
            name=self.validated_data["name"],
            phone=self.validated_data["phone"],
            birth_date=self.validated_data["birth_date"],
            address=self.validated_data["address"],
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        style={"input_type": "password"}, required=True
    )
    new_password = serializers.CharField(
        style={"input_type": "password"}, required=True
    )

    def validate_current_password(self, value):
        if not self.context["request"].user.check_password(value):
            raise serializers.ValidationError({"current_password": "Does not match"})
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"
