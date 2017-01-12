from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from common.utils import split_tags
from ninexd.users.models import User
from posts.forms import PostForm
from posts.models import Post, Tag


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-pk']


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:list')

    def form_valid(self, form):
        user = self.request.user
        author = User.objects.get(username=user.username)

        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        post = Post(author=author, title=title, content=content)
        tags_text = form.cleaned_data['tags']
        post.save()
        tag_names = split_tags(tags_text)
        for tag_name in tag_names:
            try:
                tag = Tag.objects.get(name=tag_name)
            except Tag.DoesNotExist:
                Tag.objects.create(name=tag_name)
                tag = Tag.objects.get(name=tag_name)
            post.tags.add(tag)
        return super(PostCreate, self).form_valid(form)
