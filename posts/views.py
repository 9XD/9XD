from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

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
        form.cleaned_data['author'] = User.objects.get(username=user.username)
        return super(PostCreate, self).form_valid(form)
