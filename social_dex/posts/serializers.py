from posts.models import Post
from rest_framework import serializers


class PostModelSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for 'Post' instance.

    validations:
    - content: The word 'hack' is forbidden.
    """

    user = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'

    def validate_content(self, value):
        if "hack" in value.lower():
            raise serializers.ValidationError("Forbidden word: 'hack'")
        return value
