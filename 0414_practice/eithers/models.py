from random import choices
from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=50)
    issue_a = models.CharField(max_length=20)
    issue_b = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Comment(models.Model):
    que = models.ForeignKey(Question, on_delete=models.CASCADE)
    content =  models.CharField(max_length=200)
    pick = models.CharField(max_length=20)

    def __str__(self):
        return self.content