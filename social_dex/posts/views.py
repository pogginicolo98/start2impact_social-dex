from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from posts.forms import PostModelForm
from posts.models import Post


class PostListCreateView(LoginRequiredMixin, CreateView):
    """
    Post view for list all existing 'Posts' and create new ones.

    * Only authenticated users can view or create 'Posts'.
    """

    model = Post
    form_class = PostModelForm
    template_name = 'posts/post_list.html'

    def get_context_data(self, ** kwargs):
        # Get context in order to list all 'Post' instances

        context = super().get_context_data(**kwargs)
        context["posts"] = self.model.objects.all().order_by('-datetime')
        return context

    def form_valid(self, form):
        # Set current 'User' as author (post.user) of 'Post'

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
