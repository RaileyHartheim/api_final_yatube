from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(), slug_field='username',
        queryset=User.objects.filter()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        required=True,
        queryset=User.objects.filter()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following',)
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following'),
            message="You're already following this person."
        )]

    def validate(self, data):
        """Checks if user trying to follow themself."""
        if data['user'] == data['following']:
            raise serializers.ValidationError("You can't follow yourself.")
        return data
