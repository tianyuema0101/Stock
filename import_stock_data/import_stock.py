#import Stock.urls
import os
import sys
from import_stock_data.Intrinio import Intrinio

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Stock.settings')

import django
django.setup()

from Stock_Test.models import Stock
from Stock.settings import API_KEY

Intri = Intrinio(API_KEY)
code_list = ["AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "FB", "INTC", "CSCO", "CMCSA", "PEP", "NFLX", "NVDA"]
for code in code_list:
    response = Intri.get_stock_prices(identifier=code)
    if "data" in response:
        for stock_per_day in response["data"]:
            stock = Stock()
            stock.code = code
            stock.close_price = stock_per_day["close"]
            stock.date = stock_per_day["date"]
            stock.save()

