from rest_framework import serializers

from .models import CustomUser


class RegisterCustomUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta(object):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['date_joined', 'last_activity']


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'last_activity', 'last_login']