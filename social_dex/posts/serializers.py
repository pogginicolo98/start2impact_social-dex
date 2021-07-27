from posts.models import Post
from rest_framework import serializers


class PostModelSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for 'Post' instance.

    validations:
    - content: Prohibits the publication of any post that contains the word 'hack'.
    """

    user = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'

    def validate_content(self, value):
        if "hack" in value.lower():
            raise serializers.ValidationError("forbidden word: 'hack'")
        return value
