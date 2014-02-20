from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from trades.models import Trade
from trades.forms import TradeForm

class IndexView(generic.ListView):
    template_name = 'trades/index.html'
    context_object_name = 'latest_trades_list'

    def get_queryset(self):
        return Trade.objects.order_by('-created')[:10]

class DetailView(generic.DetailView):
    model = Trade
    template_name = 'trades/detail.html'

class CreateView(generic.CreateView):
    form_class = TradeForm
    template_name = 'trades/new_trade.html'
    success_url = '/trades'

    def form_valid(self, form):
        if form.is_valid():
            trade = form.save(commit=False)
            trade.owner = self.request.user
            trade.save()
        return super(CreateView, self).form_valid(form)
