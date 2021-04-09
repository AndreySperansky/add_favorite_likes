from django.db import models
from django.contrib.auth.models import User

class CV(models.Model):
    cv = models.CharField(max_length=200, verbose_name='Заголовок')
    employers = models.ManyToManyField(User, through='BookmarkCV', verbose_name='Работодатели')

    def __str__(self):
        return f'{self.cv}'

    def get_bookmark_count(self):
        return self.likes.all().count()


    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        ordering = ['cv']


class BookmarkCV(models.Model):
    user = models.ForeignKey(User, verbose_name='Работодатель', on_delete=models.CASCADE)
    obj = models.ForeignKey(
        CV, verbose_name='Резюме',
        on_delete=models.CASCADE,
        related_name='likes'
    )


    def __str__(self):
        return f'{self.user.username}:{self.obj.cv}'

    # def get_bookmark_count(self):
    #     return self.likes.all().count()


    class Meta:
        verbose_name = 'Закладка'
        verbose_name_plural = 'Закладки'
        ordering = ['user', 'obj']


