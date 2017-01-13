from django.views.generic import DetailView
from django.views.generic import ListView
from pure_pagination import PaginationMixin

from notice.models import Notice


class NoticeList(PaginationMixin, ListView):
    model = Notice
    context_object_name = 'notice_list'
    paginate_by = 10
    paginate_orphans = 5
    ordering = ['-pk']


class NoticeDetail(DetailView):
    model = Notice
    context_object_name = 'notice'
