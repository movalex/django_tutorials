from django.http import HttpResponse


HTML = """
<H1>Hello</H1>
"""


def home_view(request):
    print(request)
    return HttpResponse(HTML)