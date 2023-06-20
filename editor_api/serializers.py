from rest_framework import serializers
from conference.models.conference_models import Conference

class AddProgramSerializer(serializers.ModelSerializer):
    """
    Serializer for AddProgramme
    """

    class Meta:
        model = Conference
        fields = "__all__"