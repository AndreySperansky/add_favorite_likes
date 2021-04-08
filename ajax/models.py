from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    favourite = models.ManyToManyField(User, verbose_name='Избранное')


    def __str__(self):
        return f'{self.favourite}: {self.title}'

    def get_bookmark_count(self):
        return self.favourite.all().count()


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

