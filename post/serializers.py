from rest_framework import serializers

from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'date_created']

    def create(self, validated_data):
        validated_data['author'] = self.context.get('request').user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.edited = True
        return super().update(instance, validated_data)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'date_created']


class LikesAmountAnalyticSerializer(serializers.ModelSerializer):
    day = serializers.DateTimeField()
    count = serializers.IntegerField()