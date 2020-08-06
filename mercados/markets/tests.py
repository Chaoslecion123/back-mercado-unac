from django.test import TestCase
from .models import *
from ..addresses.models import Address
from ..staff.models import Staff

class MarketTestCase(TestCase):
    def setUp(self):
        a1 = Address.objects.create(line_1="santos majaro",line_2="surco")
        staff = Staff.objects.create(pk=1)
        Market.objects.create(name="MERCADO UNAC" ,address=a1,staff=staff,aforo=300,count_aforo=0)

    def test_market_staf(self):
        market1 = Market.objects.get(name="MERCADO UNAC")
        self.assertEqual(market1.name,"MERCADO UNAC")
