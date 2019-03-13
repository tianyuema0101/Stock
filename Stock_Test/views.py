from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from .models import Stock
from .serializers import StockSerializer
from .filters import StockFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.http.response import HttpResponse
from django.shortcuts import render

from plotly.offline import plot
import plotly.graph_objs as go
# Create your views here.
class StockViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = StockFilter

def index(request):
    html = TemplateResponse(request, 'max_profit.html')
    return HttpResponse(html.render())


def max_profit(request):
    if request.method == 'POST':
        code = request.Post.get('code')
        start_date = request.Post.get('start_date')
        end_data = request.Post.get('end_date')
        print(start_date)
        data = {'max_profit': "5555555"}
        return JsonResponse(data)


def input_page(request):
    return render(request, 'input_page.html')


def max_profit(request):
    if request.method == 'POST':
        code= request.POST.get('code')
        start= request.POST.get('start')
        end= request.POST.get('end')
        stock_list = Stock.objects.filter(code=code, date__range=[start, end]).order_by('date')
        max_profit = 0
        buy_price = float("inf")
        init_buy_day = None
        buy_date = None
        sell_date = None
        for stock in stock_list:
            if stock.close_price <= buy_price:
                buy_price = stock.close_price
                init_buy_day = stock.date

            else:
                profit = stock.close_price - buy_price
                if profit > max_profit:
                    max_profit = profit
                    sell_date = stock.date
                    buy_date = init_buy_day
        date_list =[]
        price_list =[]
        max_profit_dates = []
        max_profit_price_range =[]
        for stock in stock_list:
            date_list.append(stock.date)
            price_list.append(stock.close_price)
            if stock.date >= buy_date and stock.date <= sell_date:
                max_profit_dates.append(stock.date)
                max_profit_price_range.append(stock.close_price)

        trace1 = go.Scatter(
            x=date_list,
            y=price_list,
            name='close price',
            mode='lines+markers',
        )

        trace2 = go.Scatter(
            x=max_profit_dates,
            y=max_profit_price_range,
            name='max profit price range',
            mode='lines+markers',
        )

        layout = dict(title = 'Max Profit',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Close Price'),
              )

        data = [trace1, trace2]
        fig = go.Figure(data=data, layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False, show_link=False)

        context = {'max_profit': max_profit, 'buy_date': buy_date, 'sell_date': sell_date, "plot": plot_div}

    return render(request, 'max_profit.html', context)
