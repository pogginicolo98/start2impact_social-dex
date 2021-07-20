from django.views.generic import TemplateView
from django.views.generic.list import ListView
from posts.models import Post

class HomepageView(TemplateView):
    """
    ???
    """

    template_name = 'posts/homepage.html'


class PostsListView(ListView):
    """
    ???
    """

    queryset = Post.objects.all().order_by('-datetime')
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
