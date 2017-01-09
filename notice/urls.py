from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.NoticeList.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>\d+)$',
        view=views.NoticeDetail.as_view(),
        name='detail'
    )
]
