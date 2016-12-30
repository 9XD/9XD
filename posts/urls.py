from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.PostList.as_view(),
        name='list'
    ),

    url(
        regex=r'^create$',
        view=views.PostCreate.as_view(),
        name='create'
    ),
]
