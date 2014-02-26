import datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import User

import factory

from models import Trade, Category, TradeType, TradeDuration, Server, Item


class TradeFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Trade

    title = factory.Sequence(lambda n: 'test_trade%d' % n)
    body = "Test Body"
    created = datetime.datetime.now
    quantity = 1
    start_price = 1
    buyout_price = 1
    server = factory.SubFactory('trades.factories.ServerFactory')
    category = factory.SubFactory('trades.factories.CategoryFactory')
    trade_type = factory.SubFactory('trades.factories.TradeTypeFactory')
    trade_duration = factory.SubFactory('trades.factories.TradeDurationFactory')
    owner = factory.SubFactory('trades.factories.UserFactory')


class UserFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = User

    first_name = 'John'
    last_name = 'Doe'
    is_staff = False
    username = factory.Sequence(lambda n: 'testuser%d' % n)
    email = factory.Sequence(lambda n: 'testuser%d@example.com' % n)

class CategoryFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Category

    title = factory.Sequence(lambda n: 'test_Category%d' % n)

class TradeTypeFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = TradeType

    title = factory.Sequence(lambda n: 'test_TradeType%d' % n)

class TradeDurationFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = TradeDuration

    title = factory.Sequence(lambda n: 'test_TradeDuration%d' % n)

class ItemFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Item

    title = factory.Sequence(lambda n: 'test_Item%d' % n)

class ServerFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Server

    title = factory.Sequence(lambda n: 'test_Server%d' % n)
