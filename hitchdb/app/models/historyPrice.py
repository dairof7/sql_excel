from django.db import models
from app.models.product import Product


class HistoryPrice(models.Model):
    price = models.CharField('Price', max_length=150, default='0')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'HistoryPrice'
        verbose_name_plural = 'History Prices'
        
    def __str__(self):
        return str(self.product) + ' - ' + str(self.price)