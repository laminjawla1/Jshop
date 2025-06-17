from rest_framework import serializers


class TenantSignupSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=32)
    last_name = serializers.CharField(max_length=32)

    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=11)

    password = serializers.CharField(min_length=8, max_length=20, write_only=True)

    business_name = serializers.CharField(max_length=100)
    domain_name = serializers.CharField(max_length=100)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=20, write_only=True)
