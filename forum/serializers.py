from rest_framework import serializers
from .models import Post, Reply


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'post', 'content', 'created_at', ]

    def create(self, validated_data):
        return super().create(validated_data)


class ForumSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)
    # likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at',
                  'replies']

    # def get_likes_count(self, obj):
    #     return obj.likes.count()

    # def validate_likes(self, value):
    #     user = self.context['request'].user
    #     if user in value.all():
    #         raise serializers.ValidationError(
    #             "You have already liked this forum.")
    #     return value