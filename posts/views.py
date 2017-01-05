import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from posts.forms import PostForm
from posts.models import Post, Tag


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:list')

    def form_valid(self, form):
        author = self.request.user
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        tags_text = form.cleaned_data['tags']
        split_tags = re.split(',\s|,|\s', tags_text)
        tags = []
        for tag_name in split_tags:
            try:
                tag = Tag.objects.get(name=tag_name)
            except Tag.DoesNotExist:
                tag = Tag.objects.create(name=tag_name)
            tags.append(tag)

        Post.objects.create(
            author=author, title=title, content=content)
        super.form_valid(form)
