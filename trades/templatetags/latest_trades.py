from django import template

from trades.models import Trade

register = template.Library()

@register.inclusion_tag('trades/latest_trades.html')
def latest_trades(takes_context=True):
    trades = Trade.objects.order_by('-created')[:10]
    return { 'trades': trades }
