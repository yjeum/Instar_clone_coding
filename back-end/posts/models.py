from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    uesr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='like_posts'
        )


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.BooleanField()