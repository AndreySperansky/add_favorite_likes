from django.shortcuts import render
import json
from django.contrib import auth
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views import View
from .models import CV, BookmarkCV


def index_view(request):

    articles = CV.objects.all()

    context = {
        "articles": articles
    }

    return render(request, 'ajax/index.html', context)


# @login_required
def add_remove_bookmark(request, pk):

    # user = request.session.get('user')
    user = request.user
    try:
        bookmark = BookmarkCV.objects.get(user=user, pk=pk)
        bookmark.delete()
    except:
        bookmark = BookmarkCV.objects.create(
            user=user,
            cv=CV.objects.get(id=pk))
        bookmark.save()
    return HttpResponseRedirect('')
