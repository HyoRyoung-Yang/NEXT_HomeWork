from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    date = models.DateTimeField(default='')

    def __str__(self):
        return self.title

class Comment(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(default='')