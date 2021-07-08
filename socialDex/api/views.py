# from django.shortcuts import render
from django.http import JsonResponse
from api.models import Post
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def posts(request):
    response = {}
    posts = Post.objects.filter().order_by('-datetime')

    for post in posts:
        response[f'{post.pk}'] = {
            'datetime': post.datetime,
            'content': post.content,
            'author': f'{post.user.first_name} {post.user.last_name}',
            'hash': post.hash,
            'tx_id': post.tx_id
        }
    return JsonResponse(response)


class NewPost(APIView):
    permission_classes = (IsAuthenticated,)

    def new_post(self, request):
        if request.method == 'POST':
            user = request.user
            content = request.POST.get('content', None)
            print(f'il messaggio è: {content}\nuser è: {user}')
            return Response(data={'status': True})
            # if user and content:
            #     post = Post(user=user, content=content)
            #     post.save()
            #     posts(request)
            # else:
            #     return JsonResponse({'error': 'not_enough_data', 'request_data': request.data})
        return JsonResponse({'error': 'not_post'})
