from django.test import TestCase, Client
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import utc

from trades.models import Trade
from trades.views import *
from trades.factories import *


class TradesViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testuser')
        trades = []
        for _ in xrange(25):
            trades.append(TradeFactory(owner=self.user))

    def test_trades_listing_route(self):
        response = self.client.get('/trades/')
        self.assertEquals(response.status_code, 200)

    def test_trades_detail_route(self):
        trade = TradeFactory(owner=self.user)
        response = self.client.get('/trades/%d/' % trade.id)
        self.assertEquals(response.status_code, 200)


class NewTradeTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testuser')
        self.client.login(username='testuser', password='testuser')

    def test_new_trades_route(self):
        response = self.client.get('/trades/new')
        self.assertEquals(response.status_code, 200)

    def test_create_new_trade_and_save(self):
        created = datetime.datetime.utcnow().replace(tzinfo=utc)
        server = ServerFactory()
        category = CategoryFactory()
        trade_type = TradeTypeFactory()
        trade_duration = TradeDurationFactory()

        self.client.post(
            '/trades/new',
            data={
                'title': 'A new trade',
                'body': 'This is the description of a new test trade. It might later even contain images!',
                'created': created,
                'owner': self.user,
                'quantity': 1,
                'start_price': 1,
                'buyout_price': 1,
                'server': server.id,
                'category': category.id,
                'trade_type': trade_type.id,
                'trade_duration': trade_duration.id,
            }
        )

        self.assertEqual(Trade.objects.count(), 1)
        new_trade = Trade.objects.first()
        self.assertEqual(new_trade.title, 'A new trade')
        self.assertEqual(new_trade.body, 'This is the description of a new test trade. It might later even contain images!')
        self.assertEqual(new_trade.owner, self.user)
        self.assertEqual(new_trade.quantity, 1)
        self.assertEqual(new_trade.start_price, 1)
        self.assertEqual(new_trade.buyout_price, 1)
        self.assertEqual(new_trade.server, server)
        self.assertEqual(new_trade.category, category)
        self.assertEqual(new_trade.trade_type, trade_type)
        self.assertEqual(new_trade.trade_duration, trade_duration)
