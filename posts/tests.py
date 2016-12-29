from test_plus.test import TestCase

from posts.factories import PostFactory


class PostsTest(TestCase):
    def test_get_posts_list(self):
        post = PostFactory()
        post_list_url = self.reverse("post:list")
        self.get_check_200(post_list_url)
        self.assertResponseContains(post.title, html=False)
        self.assertResponseContains(post.author.name, html=False)
