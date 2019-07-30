from django.db import models

# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length=200)
    pubData = models.DateTimeField('date Publihed')
    body = models.TextField()

    def __str__(self):
        return self.title