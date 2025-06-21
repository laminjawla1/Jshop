from rest_framework import serializers
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException


class TenantSignupSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=32)
    last_name = serializers.CharField(max_length=32)

    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=16)

    password = serializers.CharField(min_length=8, max_length=20, write_only=True)

    business_name = serializers.CharField(max_length=100)
    subdomain = serializers.CharField(max_length=100)

    def validate_phone_number(self, value):
        try:
            parsed = phonenumbers.parse(value, "GM")
            # Check if number is valid by Google's data
            if phonenumbers.is_valid_number(parsed):
                return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
            else:
                # Custom logic: accept 7-digit local numbers starting with 4
                national_number = str(parsed.national_number)
                if len(national_number) == 7 and national_number.startswith("4"):
                    return "+220" + national_number
                raise serializers.ValidationError("Phone number is invalid.")
        except NumberParseException:
            raise serializers.ValidationError("Phone number is invalid.")
        
    def validate_subdomain(self, value):
        import re
        if not re.match(r'^[a-z]+$', value):
            raise serializers.ValidationError(
                "Domain name must contain only lowercase letters with no numbers or special characters."
            )
        return value.lower()

