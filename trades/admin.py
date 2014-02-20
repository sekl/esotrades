from django.contrib import admin
from trades.models import Trade, Item, Category, Server, TradeType, TradeDuration

admin.site.register((Trade, Item, Category, Server, TradeType, TradeDuration))
