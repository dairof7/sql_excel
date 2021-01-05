from django.db import models
from app.models.countries import Country


class Retailer(models.Model):
    retailer = models.CharField('Retailer', max_length=150, unique=True, blank=False)
    image = models.TextField('URL Image', blank=True, null=True)
    # image = models.ImageField('Image', upload_to=None, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Retailer'
        verbose_name_plural = 'Retailers'
        
    def __str__(self):
        return str(self.retailer)