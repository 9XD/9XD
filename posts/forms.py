from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, Textarea
from markdown2 import Markdown

from common.utils import split_tags
from posts.models import Post, Tag


class PostForm(ModelForm):
    content = CharField(widget=Textarea(
        attrs={
            ':value': 'input',
            '@input': 'update'
        }
    ))
    tags = CharField()

    def clean_tags(self):
        tags_text = self.cleaned_data['tags']
        tag_names = split_tags(tags_text)
        for tag_name in tag_names:
            tag_name.strip()
            if len(tag_name) < 0 or len(tag_name) > 16:
                raise ValidationError("Tag is too long.")

        return tags_text

    def save(self, commit=True):
        author = self.cleaned_data['author']
        title = self.cleaned_data['title']
        content = self.cleaned_data['content']
        markdown = Markdown()
        html = markdown.convert(content)
        post = Post(author=author, title=title, content=content, html=html)
        post.save()

        tags_text = self.cleaned_data['tags']
        tag_names = split_tags(tags_text)
        for tag_name in tag_names:
            tag_name.strip()
            if 0 < len(tag_name) < 16:
                tag = self.create_and_get(tag_name)
                post.tags.add(tag)

        return self.instance

    @staticmethod
    def create_and_get(tag_name):
        try:
            tag = Tag.objects.get(name=tag_name)
        except Tag.DoesNotExist:
            Tag.objects.create(name=tag_name)
            tag = Tag.objects.get(name=tag_name)
        return tag

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'is_public']


