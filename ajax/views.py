from django.shortcuts import render
import json
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views import View
from .models import Article


def index_view(request):
    context = {
        "articls": Article.objects.all(),
        "title": "Article_List"
    }
    return render(request, 'ajax/index.html', context)


class BookmarkView(View):
    # в данную переменную будет устанавливаться модель закладок, которую необходимо обработать
    model = Article


    def post(self, request, pk):
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
                "count": self.model.objects.filter(obj_id=pk).count()
            }),
            content_type="application/ajax"
        )






