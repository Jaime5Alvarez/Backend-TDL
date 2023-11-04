from ..models import MyUser
from rest_framework import serializers

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'password')
    def validate(self, data):
        if len(data['password']) < 4:
            raise serializers.ValidationError('Password must be at least 4 characters long')
        return data
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = MyUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        
        return user