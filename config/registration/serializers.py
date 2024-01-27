from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    """Serializer for user model"""

    class Meta:
        model = User
        fields = ("id", "username", "password")

