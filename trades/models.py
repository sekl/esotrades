from django.db import models

class Trade(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
