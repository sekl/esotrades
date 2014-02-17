from django.contrib import admin
from trades.models import Trade, Item

admin.site.register((Trade, Item))
