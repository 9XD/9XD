from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import ListView

from posts.models import Post


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'tags']
