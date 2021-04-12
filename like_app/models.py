from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    body = models.TextField()
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')



    def __str__(self):
        return f'{self.title}:{self.author.username}'

    @property
    def num_likes(self):
        return self.likes.all().count()


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title', 'author', '-created_at']


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)
    # is_favorite = models.BooleanField(default=False)



    def __str__(self):
        return f'{self.user.username}:{self.post.title}'


    class Meta:
        verbose_name = 'Закладка'
        verbose_name_plural = 'Закладки'
        ordering = ['user', 'value']


