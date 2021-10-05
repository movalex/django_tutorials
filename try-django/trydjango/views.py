from django.http import HttpResponse

from articles.models import Article


def home_view(request):
    article_obj = Article.objects.get(id=2)
    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    HTML_STRING = f"""
    <H1>{article_obj.title}</H1>
    
    <p>{article_obj.content}</p>
    """.format(**context)

    return HttpResponse(HTML_STRING)
