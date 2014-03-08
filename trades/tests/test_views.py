from django.template.loader import render_to_string
from django.test import TestCase, Client
from django.contrib.auth.models import User

from trades.models import Trade
from trades.views import *
from trades.factories import *


class TradesViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username='testuser', password='testuser')
        trades = []
        for _ in xrange(25):
            trades.append(TradeFactory(owner=user))

    def test_trades_listing_route(self):
        response = self.client.get('/trades/')
        self.assertEquals(response.status_code, 200)

    def test_trades_detail_route(self):
        response = self.client.get('/trades/1/')
        self.assertEquals(response.status_code, 200)


class NewTradeTest(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username='testuser', password='testuser')

    def test_new_trades_route(self):
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/trades/new')
        self.assertEquals(response.status_code, 200)
