# from django.shortcuts import render
from django.http import JsonResponse
from api.models import Post


def posts(request):
    response = {}
    posts = Post.objects.filter().order_by('-datetime')

    for post in posts:
        response[f'{post.pk}'] = {
            'datetime': post.datetime,
            'content': post.content,
            'author': f'{post.user.first_name} {post.user.last_name}'
        }
    return JsonResponse(response)
