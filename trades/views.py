from django.shortcuts import render, get_object_or_404

from trades.models import Trade

def index(request):
    latest_trades_list = Trade.objects.order_by('created')[:10]
    context = { 'latest_trades_list': latest_trades_list }
    return render(request, 'trades/index.html', context)

def detail(request, trade_id):
    trade = get_object_or_404(Trade, pk=trade_id)
    return render(request, 'trades/detail.html', { 'trade': trade })
