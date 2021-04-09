from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    readers = models.ManyToManyField(User, through='BookmarkArticle', verbose_name='Читатели')

    def __str__(self):
        return f'{self.title}'

    def get_bookmark_count(self):
        return self.likes.all().count()


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title']


class BookmarkArticle(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    obj = models.ForeignKey(
        Article, verbose_name='Статья',
        on_delete=models.CASCADE,
        related_name='likes'
    )


    def __str__(self):
        return f'{self.user.username}:{self.obj.title}'

    # def get_bookmark_count(self):
    #     return self.likes.all().count()


    class Meta:
        verbose_name = 'Закладка'
        verbose_name_plural = 'Закладки'
        ordering = ['user', 'obj']


