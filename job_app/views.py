from django.shortcuts import render
import json
from django.contrib import auth
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from .models import Job, BookmarkJob


def index_view(request):

    vacancies = Job.objects.all()

    context = {
        "vacancies": vacancies,
    }

    return render(request, 'job_app/index.html', context)




def add_remove_bookmark(request, pk):
    user = request.user

    try:
        bookmark = BookmarkJob.objects.get(user=user, obj=pk)
        bookmark.delete()
    except:
        bookmark = BookmarkJob.objects.create(
            user=user,
            obj=Job.objects.get(id=pk))
        bookmark.save()
    return HttpResponseRedirect(reverse('job_app:index'))
        # return redirect('job_app:index')









# @login_required
# def add_remove_bookmark(request, pk):
#
#     if request.is_ajax():
#     # user = request.session.get('user')
#         user = request.user
#         try:
#             bookmark = BookmarkJob.objects.get(user=user, obj=pk)
#             bookmark.delete()
#         except:
#             bookmark = BookmarkJob.objects.create(
#                 user=user,
#                 obj=Job.objects.get(id=pk))
#             bookmark.save()
#
#         data = {'bookmark': bookmark}
#         result = render_to_string('job_app/includes/inc_favorits.html', data)
#         context = {'result': result}
#
#         return JsonResponse(context)



# асинхронный вариант
# def favorite_project(request, albom_id):
#     projectprofile = get_object_or_404(ProjectProfile, pk=albom_id)
#     # try:
#     if projectprofile.is_favorite:
#         projectprofile.is_favorite = False
#     else:
#         projectprofile.is_favorite = True
#     projectprofile.save()
#     return HttpResponseRedirect(reverse('mainapp:index'))