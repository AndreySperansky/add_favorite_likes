# Generated by Django 3.1.7 on 2021-04-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like_app', '0002_auto_20210413_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10, verbose_name='Лайк'),
        ),
    ]