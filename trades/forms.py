from django import forms
from trades.models import Trade, Category, Server, TradeType, TradeDuration


class TradeForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label='Title:')
    server = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Server:',
    )
    trade_type = forms.ModelChoiceField(
        queryset=TradeType.objects.all(),
        label='Type:',
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Category:',
    )
    trade_duration = forms.ModelChoiceField(
        queryset=TradeDuration.objects.all(),
        label='Duration:',

    )
    quantity = forms.IntegerField(label='Quantity:')
    start_price = forms.IntegerField(label='Start Price:')
    buyout_price = forms.IntegerField(label='Buyout Price:')
    body = forms.Textarea()

    class Meta:
        model = Trade
