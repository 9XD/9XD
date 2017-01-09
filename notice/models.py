from django.db import models
from model_utils.models import TimeStampedModel

from ninexd.users.models import User


class Notice(TimeStampedModel):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=60)
    content = models.TextField()
    views = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)
