from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import auth
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View
from .models import Article


def index_view(request):
    context = {
        "articls": Article.objects.all(),
    }
    return render(request, 'ajax/index.html', context)


def favorites_edit(request, pk):
    print(request, pk)

    if request.is_ajax():
        # нам потребуется пользователь
        # user = auth.get_user(request)
        # пытаемся получить закладку из таблицы, или создать новую
        bookmark = Article.objects.get_object_or_404(user=request.user, pk=pk)
        print(bookmark)

        # если не была создана новая закладка,
        # то считаем, что запрос был на удаление закладки

            # bookmark.delete()



        articles = Article.objects.filter(user=request.user)
        print(articles)
        context = {
            'articles': articles,
            "count": Article.objects.filter(pk=pk).count(),
         }
        print(context)

        result = render_to_string('ajax/includes/inc_favorits.html', context)
        return JsonResponse({'result': result})

