from rest_framework import serializers

from videos.models.key import APIKey


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = "__all__"
