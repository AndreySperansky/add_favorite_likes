from django.shortcuts import render
import json
from django.contrib import auth
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from .models import CV, BookmarkCV


def index_view(request):

    resumes = CV.objects.all()

    context = {
        "resumes": resumes
    }

    return render(request, 'cv_app/index.html', context)


# @login_required
def add_remove_bookmark(request, pk):

    # user = request.session.get('user')
    user = request.user
    try:
        bookmark = BookmarkCV.objects.get(user=user, obj=pk)
        bookmark.delete()
    except:
        bookmark = BookmarkCV.objects.create(
            user=user,
            obj=CV.objects.get(id=pk))
        bookmark.save()
    return HttpResponseRedirect(reverse('cv_app:index'))
