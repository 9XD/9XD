from django.db import models
from model_utils.models import TimeStampedModel

from ninexd.users.models import User


class Tag(models.Model):
    name = models.CharField(max_length=16)


class Post(TimeStampedModel):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=60)
    content = models.TextField()
    views = models.IntegerField()
    is_public = models.BooleanField()
    tags = models.ManyToManyField(Tag)
