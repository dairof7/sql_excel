from django.db import models
from app.models.hitchModel import HitchModel
from app.models.retailers import Retailer
from app.models.countries import Country




class Product(models.Model):
    url = models.TextField('URL')
    # image = models.CharField('Image URL', max_length=255)
    current_price = models.CharField('Current Price', max_length=50)
    enable = models.BooleanField('Enable', default=True)
    issue_report = models.BooleanField('Issue Report', default=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    hitch_model = models.ForeignKey(HitchModel, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return str(self.hitch_model) + ' - ' + str(self.retailer)