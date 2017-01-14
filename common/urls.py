from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(
        regex=r'^convert-markdown$',
        view=views.convert_markdown,
        name='convert-markdown'
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)
