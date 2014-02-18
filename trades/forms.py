from django import forms
from trades.models import Trade

class TradeForm(forms.ModelForm):
    title = forms.CharField(max_length=255, help_text="Please enter a title.")
    body = forms.Textarea()

    class Meta:
        model = Trade
