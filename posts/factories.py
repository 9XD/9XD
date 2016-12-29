from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyText

from ninexd.users.tests.factories import UserFactory
from posts.models import Post, Tag


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    author = SubFactory(UserFactory)
    title = 'This is Jelly'
    content = 'jelly jelly jelly is delicious yeah yeah'
    views = FuzzyInteger(0, 2000)
    is_public = True


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = FuzzyText(length=10)





