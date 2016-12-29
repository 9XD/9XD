from test_plus.test import TestCase


class HomeTest(TestCase):
    def test_get_home(self):
        home_url = self.reverse('home')
        self.get_check_200(home_url)
        self.assertResponseContains('<title>9XD</title>')

