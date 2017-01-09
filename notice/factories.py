import factory
from factory import SubFactory

from ninexd.users.tests.factories import UserFactory
from notice.models import Notice


class NoticeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notice

    author = SubFactory(UserFactory)
    title = 'Welcome to new 9XD Site'
    content = "<h2>This is new generation</h2><p>yeah yeah</p>"
    is_public = True
