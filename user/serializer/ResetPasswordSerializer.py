from rest_framework import serializers

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2, max_length=255)

    class Meta:
        fields=['email']