from django.urls import reverse
from test_plus.test import TestCase

from posts.factories import PostFactory


class PostsTest(TestCase):
    def test_get_list(self):
        # given
        post = PostFactory()
        post_list_url = self.reverse('posts:list')
        # when
        self.get_check_200(post_list_url)
        # then
        self.assertResponseContains(post.title, html=False)
        self.assertResponseContains(post.author.name, html=False)
        write_url = self.reverse('posts:create')
        self.assertResponseContains(write_url, html=False)

    def test_get_writing_page_with_login(self):
        # given
        user = self.make_user('jelly_jelly')
        # when
        with self.login(username=user.username):
            # then
            write_post_url = self.reverse('posts:create')
            self.get_check_200(write_post_url)

    def test_get_writing_page_with_anonymous(self):
        self.assertLoginRequired('posts:create')

    def test_post_writing(self):
        # given
        user = self.make_user('jelly_jelly')
        data = {
            "title": "This is some ",
            "content": "This is exactly contents.",
            "tags": "ARSTSTRST, arsiten, 태그태그",
        }
        # when
        with self.login(username=user.username):
            write_post_url = self.reverse('posts:create')
            # then
            self.get_check_200(write_post_url)
            self.post('post:write', data=data)

    def test_get_detail_page(self):
        # given
        post = PostFactory()
        detail_url = reverse('posts:detail', kwargs={'pk': post.pk})
        self.get_check_200(detail_url)
        # when then
        self.assertResponseContains(post.author.username, html=False)
        self.assertResponseContains(post.title, html=False)
        self.assertResponseContains(post.content, html=False)
