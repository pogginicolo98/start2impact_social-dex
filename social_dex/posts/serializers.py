from posts.models import Post
from rest_framework import serializers


class PostModelSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for 'Post' instance.
    """

    user = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'
