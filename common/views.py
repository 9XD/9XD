from django.http import HttpResponse
from markdown2 import Markdown


def convert_markdown(request):
    markdown = Markdown()
    converted_string = markdown.convert(request.POST['text'])
    return HttpResponse(converted_string)

