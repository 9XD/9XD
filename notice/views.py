from django.views.generic import DetailView
from django.views.generic import ListView

from common.views import LimitedPageMixin
from notice.models import Notice


class NoticeList(LimitedPageMixin, ListView):
    model = Notice
    context_object_name = 'notice_list'
    paginate_by = 10
    paginate_orphans = 5
    range_length = 10
    ordering = ['-pk']


class NoticeDetail(DetailView):
    model = Notice
    context_object_name = 'notice'
