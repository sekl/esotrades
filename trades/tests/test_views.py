from django.template.loader import render_to_string
from django.test import TestCase, Client

from trades.models import Trade
from trades.views import *
from trades.factories import *

class ViewTest(TestCase):
    def setUp(self):
        self.client_stub = Client()
        user = UserFactory()
        trades = []
        for _ in xrange(25):
            trades.append(TradeFactory(owner=user))

    def test_view_trades_listing_route(self):
        response = self.client_stub.get('/trades/')
        self.assertEquals(response.status_code, 200)

    def test_view_trades_detail_route(self):
        response = self.client_stub.get('/trades/1/')
        self.assertEquals(response.status_code, 200)

    def test_view_trades_new_route(self):
        # this will fail for now due to missing login
        response = self.client_stub.get('/trades/new')
        self.assertEquals(response.status_code, 200)
