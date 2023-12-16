from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=300, default='name')
    text = models.TextField(default='')
    date_of_creation = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='authors')
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def to_json(self):
        return self.title
