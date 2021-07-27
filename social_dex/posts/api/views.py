from datetime import timedelta
from django.utils import timezone
from posts.api.signals import new_post_api_view_called, posts_api_view_called
from posts.models import Post
from posts.serializers import PostModelSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def posts(request):
    """
    Allowed methods: GET.
    Retrieve a list of all 'Post' instances
    or retrieve the number of posts that contain a keyword passed as 'search' parameter.

    * Only authenticated users can retrieve data.
    """

    if 'search' in request.GET:
        # URL contains 'search'
        querystring = request.GET.get('search')
        if len(querystring) == 0:
            context = {
                'error': "'search' parameter must be not null"
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        number_of_posts = Post.objects.filter(content__icontains=querystring).count()
        context = {
            'posts found': number_of_posts
        }
        return Response(context, status=status.HTTP_200_OK)
    else:
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


class LatestPostListAPIView(generics.ListAPIView):
    """
    An APIView that provides 'list()' action.
    Retrieve a list with all 'Posts' published in the last hour.
    """

    serializer_class = PostModelSerializer

    def get_queryset(self):
        """
        Override 'get_queryset()' method of GenericAPIView class.
        """

        last_hour = timezone.now() - timedelta(hours=1)
        queryset = Post.objects.filter(datetime__gte=last_hour).order_by('-datetime')
        return queryset
