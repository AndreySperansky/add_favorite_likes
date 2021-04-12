from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from mainapp.models import ProjectProfile


def index_view(request):
    context = {
        "table_list": ProjectProfile.objects.all(),
        "title": "Albom_List"
    }
    return render(request, 'mainapp/index.html', context)



# асинхронный вариант
def favorite_project(request, albom_id):
    projectprofile = get_object_or_404(ProjectProfile, pk=albom_id)
    # try:
    if projectprofile.is_favorite:
        projectprofile.is_favorite = False
    else:
        projectprofile.is_favorite = True
    projectprofile.save()
    return HttpResponseRedirect(reverse('mainapp:index'))




