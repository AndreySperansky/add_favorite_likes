from django.contrib.auth.models import User
from django.db import models

class ProjectProfile(models.Model):
    project_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Профиль Проекта'
        verbose_name_plural = 'Профили Проекта'



