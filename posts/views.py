from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from common.utils import split_tags
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

        tag_names = split_tags(tags_text)
        tags = []
        for tag_name in tag_names:
            try:
                tag = Tag.objects.get(name=tag_name)
            except Tag.DoesNotExist:
                tag = Tag.objects.create(name=tag_name)
                tag.save()
            tags.append(tag)

        Post.objects.create(
            author=author, title=title, content=content, tags=tags)
        super(CreateView, self).form_valid(form)
