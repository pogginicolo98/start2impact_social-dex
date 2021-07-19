from api.models import Post
from api.serializers import PostModelSerializer
from api.signals import new_post_api_view_called, posts_api_view_called
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def posts(request):
    """
    Allowed methods: GET.
    Retrieve a list of all 'Post' instances.

    * Only authenticated users can request data.
    """

    post_list = Post.objects.all().order_by('-id')
    serializer = PostModelSerializer(post_list, many=True)
    posts_api_view_called.send(sender='posts', request=request)  # Send signal in order to register user's activity
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_post(request):
    """
    Allowed methods: POST.
    Create a new 'Post' instance with received data.

    * Only authenticated users can create new 'Post' instances.
    """

    serializer = PostModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        new_post_api_view_called.send(sender='new-post', request=request)  # Send signal in order to register user's activity
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

