import datetime
from django.db import models
from django.contrib.auth.models import User

class Trade(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, editable=False, default=None)
    quantity = models.IntegerField(blank=False, default=0)
    start_price = models.IntegerField(default=1)
    buyout_price = models.IntegerField(blank=False, default=1)
    server = models.ForeignKey('Server', blank=False, null=True)
    category = models.ForeignKey('Category', blank=False, null=True)
    trade_type = models.ForeignKey('TradeType', blank=False, null=True)
    trade_start_time = models.DateTimeField(blank=False, default=datetime.datetime.now)
    trade_duration = models.ForeignKey('TradeDuration', blank=False, null=True)

    def __unicode__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class Server(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class TradeType(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class TradeDuration(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

