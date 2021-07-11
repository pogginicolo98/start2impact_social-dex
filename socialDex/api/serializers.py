from api.models import Post
from rest_framework.serializers import ModelSerializer


class PostModelSerializer(ModelSerializer):
    """
    ModelSerializer for 'Post' instance.
    """

    class Meta:
        model = Post
        fields = '__all__'
