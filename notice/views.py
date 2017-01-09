from django.views.generic import DetailView
from django.views.generic import ListView

from notice.models import Notice


class NoticeList(ListView):
    model = Notice
    context_object_name = 'notice_list'
    paginate_by = 10
    ordering = ['-pk']


class NoticeDetail(DetailView):
    model = Notice
    context_object_name = 'notice'
