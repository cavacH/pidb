from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    category = models.IntegerField()
    description = models.TextField()
    put_time = models.DateField(auto_now_add=True)