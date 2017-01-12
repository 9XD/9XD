from test_plus.test import TestCase

from posts.factories import PostFactory


class PostsTest(TestCase):
    def test_get_list(self):
        # given
        post = PostFactory()
        post_list_url = self.reverse('post:list')
        # when
        self.get_check_200(post_list_url)
        # then
        self.assertResponseContains(post.title, html=False)
        self.assertResponseContains(post.author.name, html=False)
        write_url = self.reverse('post:create')
        self.assertResponseContains(write_url, html=False)

    def test_get_writing_page_with_login(self):
        # given
        user = self.make_user('jelly jelly')
        # when
        with self.login(username=user.username):
            # then
            write_post_url = self.reverse('post:create')
            self.get_check_200(write_post_url)

    def test_get_writing_page_with_anonymous(self):
        self.assertLoginRequired('post:create')

    def test_post_writing(self):
        # given
        user = self.make_user('jelly_jelly')
        data = {"title", "This is some "}
        # when
        with self.login(username=user.username):
            write_post_url = self.reverse('post:create')
            # then
            self.get_check_200(write_post_url)
            self.post('post:write', data=data)

    def test_get_detail_page(self):
        # given
        PostFactory()
        self.get_check_200('post:detail')
        # when then
        self.assertResponseContains(PostFactory.author)
        self.assertResponseContains(PostFactory.title)
        self.assertResponseContains(PostFactory.content)
