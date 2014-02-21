import datetime
from haystack import indexes
from trades.models import Trade


class TradeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='owner')
    trade_start_time = indexes.DateTimeField(model_attr='trade_start_time')

    def get_model(self):
        return Trade

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(trade_start_time__lte=datetime.datetime.now())
