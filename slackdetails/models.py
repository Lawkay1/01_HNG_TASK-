from django.db import models

class SlackDetails(models.Model):

    slackUsername = models.CharField(max_length=20, unique=True, required= True)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.CharField(max_length=300)

# Create your models here.
