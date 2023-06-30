"""
    Editor API Serializers
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from conference.models.conference_models import Conference


class AddConferenceSerializer(serializers.ModelSerializer):
    """
        Serializer for AddProgramme
    """

    class Meta:
        """Meta for add conference
        """
        model = Conference
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """ 
        User Serializer
    """
    class Meta:
        """Meta for user serializer
        """
        model = User
        fields = ("id", "username", "password", "email", "first_name", "last_name")
        write_only_fields = ("password",)
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        userr = user.save()

        return userr
