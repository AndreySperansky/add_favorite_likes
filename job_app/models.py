from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    vacancy = models.CharField(max_length=200, verbose_name='Вакансия')
    liked = models.ManyToManyField(User, through='BookmarkJob', verbose_name='В избранное')

    def __str__(self):
        return f'{self.vacancy}'

    def get_bookmark_count(self):
        return self.likes.all().count()


    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'
        ordering = ['vacancy']


class BookmarkJob(models.Model):
    user = models.ForeignKey(User, verbose_name='Соискатель', on_delete=models.CASCADE)
    obj = models.ForeignKey(
        Job, verbose_name='Вакансия',
        on_delete=models.CASCADE,
        related_name='likes'
    )
    # is_favorite = models.BooleanField(default=False)



    def __str__(self):
        return f'{self.user.username}:{self.obj.vacancy}'


    class Meta:
        verbose_name = 'Закладка'
        verbose_name_plural = 'Закладки'
        ordering = ['user', 'obj']


