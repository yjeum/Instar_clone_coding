from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    uesr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='like_posts'
    )
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='like_comments'
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

