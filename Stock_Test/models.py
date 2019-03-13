from django.db import models

# Create your models here.

class Stock(models.Model):
    """
        Stock Close Price
    """

    code = models.CharField(max_length=20, verbose_name="Stock_ID")
    close_price = models.FloatField(default=0.0, verbose_name="close_price")
    date = models.DateField(verbose_name="Date")

    class Meta:
        verbose_name = "stock"
        verbose_name_plural = "stocks"

    def __str__(self):
        return str(self.code)
