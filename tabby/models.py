from django.db import models
from django.contrib.auth.models import User

class Tuser(models.Model):
    user = models.OneToOneField(User)
    status = models.IntegerField(default=0)

class Question(models.Model):
    tuser = models.ForeignKey(Tuser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.IntegerField()
    description = models.TextField()
    put_time = models.DateField(auto_now_add=True)

class Reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tuser = models.ForeignKey(Tuser, on_delete=models.CASCADE)
    put_time = models.DateField(auto_now_add=True)
    thumb_up = models.IntegerField(default=0)
    description = models.TextField()
