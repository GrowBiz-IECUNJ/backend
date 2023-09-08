from django.db import models
# from user.models import MyUser


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_likes = models.PositiveBigIntegerField(default=0)
    # likes = models.ManyToManyField(
    #     MyUser, related_name='liked_forums', blank=True)

    def __str__(self):
        return self.title


class Reply(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='replies')
    # author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f''