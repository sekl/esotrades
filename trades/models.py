from django.db import models
from django.contrib.auth.models import User

class Trade(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, blank=False, null=True)

    def __unicode__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
