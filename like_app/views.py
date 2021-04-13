from django.shortcuts import render, redirect
import json
from django.contrib import auth
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from .models import Post, Like


def index_view(request):

    posts = Post.objects.all()
    user = request.user

    context = {
        "posts": posts,
        "user": user
    }

    return render(request, 'like_app/index.html', context)




def add_remove_like(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Unlike':
                like.value = 'Like'
            else:
                like.value = 'Unlike'

        like.save()

    # return HttpResponseRedirect(reverse('like_app:index'))
    return redirect('like_app:index')









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