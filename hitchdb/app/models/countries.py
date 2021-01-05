from django.db import models


class Country(models.Model):
    country = models.CharField('Country', max_length=50, blank=False, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        
    def __str__(self):
        return str(self.country)
        