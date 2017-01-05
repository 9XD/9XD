from django.forms import ModelForm, CharField

from posts.models import Post


class PostForm(ModelForm):
    tags = CharField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'is_public']
