from django.contrib.auth.models import User
from django.db import models

class ProjectProfile(models.Model):
    project_name = models.CharField(max_length=100, verbose_name='Альбом')
    artist = models.CharField(max_length=100, verbose_name='Исполнитель')
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'



