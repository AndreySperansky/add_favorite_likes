from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from mainapp.models import ProjectProfile


def index_view(request):
    context = {
        "table_list": ProjectProfile.objects.all(),
        "title": "Table_List"
    }
    return render(request, 'mainapp/index.html', context)




def favorite_project(request, projectprofile_id):
    projectprofile = get_object_or_404(ProjectProfile, pk=projectprofile_id)
    try:
        if projectprofile.is_favorite:
            projectprofile.is_favorite = False
        else:
            projectprofile.is_favorite = True
        projectprofile.save()
    except (KeyError, ProjectProfile.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})



