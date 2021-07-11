from api.models import Post
from api.serializers import PostModelSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PostListCreateAPIView(APIView):
    """
    Retrieve a list of all 'Post' instances and create a new one.
    """

    def get(self, request):
        # Return a list of all 'Posts'

        posts = Post.objects.all()
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new 'Post' with received data and then write it on chain

        serializer = PostModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            post = get_object_or_404(Post, pk=serializer.data['id'])
            post.write_on_chain()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
