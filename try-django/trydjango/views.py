from django.http import HttpResponse
# from articles.models import Articles
#


def home_view(request):
    # article_obj = Articles.objects.get

    HTML = """
    <H1>{{}}</H1>
    """

    return HttpResponse(HTML)
