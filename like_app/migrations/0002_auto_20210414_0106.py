# Generated by Django 3.1.7 on 2021-04-13 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('like_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['user', 'value'], 'verbose_name': 'Лайк', 'verbose_name_plural': 'Лайки'},
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Читатель'),
        ),
    ]
