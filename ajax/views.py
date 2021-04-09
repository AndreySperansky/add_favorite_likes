from django.shortcuts import render
import json
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views import View
from .models import Article, BookmarkArticle


def index_view(request):

    articles = Article.objects.all()

    context = {
        "articles": articles
    }

    return render(request, 'ajax/index.html', context)


class BookmarkView(View):
    # в данную переменную будет устанавливаться модель закладок, которую необходимо обработать
    model = BookmarkArticle


    def post(self, request, pk):
        print(request)
        # нам потребуется пользователь
        # user = auth.get_user(request)
        # пытаемся получить закладку из таблицы, или создать новую
        bookmark, created = self.model.objects.get_or_create(user=request.user, pk=pk)
        # если не была создана новая закладка,
        # то считаем, что запрос был на удаление закладки
        if not created:
            bookmark.delete()

        return HttpResponse(
            json.dumps({
                "result": created,
                "count": self.model.objects.filter(pk=pk).count()
            }),
            content_type="application/ajax"
        )






