from django.urls import reverse
from test_plus import TestCase

from notice.factories import NoticeFactory


class NoticeTest(TestCase):
    def test_notice_in_navigation(self):
        self.get_check_200('home')
        self.assertResponseContains('Notice', html=False)
        self.assertResponseContains(reverse('notice:list'), html=False)

    def test_get_notice_list_page(self):
        # given
        for _ in range(20):
            NoticeFactory()
        notice = NoticeFactory()
        # when, then
        self.get_check_200(reverse('notice:list'))
        self.assertResponseContains(NoticeFactory.title, html=False)
        detail_url = reverse('notice:detail', kwargs={'pk': notice.pk})
        self.assertResponseContains(detail_url, html=False)

    def test_get_detail_page(self):
        # given
        notice = NoticeFactory()
        # when, then
        detail_url = reverse('notice:detail', kwargs={'pk': notice.pk})
        self.get_check_200(detail_url)
        self.assertResponseContains(notice.title, html=False)
        self.assertResponseContains(notice.content, html=False)
