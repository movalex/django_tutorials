from django.http import HttpResponse

from articles.models import Article
from random import randint

from django.template.loader import render_to_string
from django.template.loader import get_template  # another way to do the same


def home_view(request):
    number = randint(2, 4)
    article_obj = Article.objects.get(id=number)
    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    # use strings:

    # HTML_STRING = """
    # <H1>{title}</H1>
    # <p>{content} with id: {id}</p>
    # """.format(**context)

    html_string = render_to_string("index.html", context=context)

    # another approach:

    # tmpl = get_template("index.html")
    # html_string = tmpl.render(context=context)

    return HttpResponse(html_string)
