import requests
import json


class Intrinio(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.intrinio.com/prices?{data}&api_key={api_key}"

    def get_stock_prices(self, identifier, start_date=None, end_date=None):
        if start_date and end_date:
            data = "identifier=" + identifier + "&start_date=" + start_date + "&end_date=" + end_date
        elif start_date:
            data = "identifier=" + identifier + "start_date=" + start_date
        elif end_date:
            data = "identifier=" + identifier + "end_date=" + end_date
        else:
            data = "identifier=" + identifier
        response = requests.get(self.url.format(data=data, api_key=self.api_key))
        re_dict = json.loads(response.text)

        return re_dict