from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["id", "name", "created_at", "updated_at"]
        fields = '__all__'