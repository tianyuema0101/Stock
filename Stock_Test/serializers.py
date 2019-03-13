from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    """
    Stock serializers
    """

    class Meta:
        model = Stock
        fields = "__all__"

