from django.db import models
from app.models.users import User
from app.models.product import Product

class Tracking(models.Model):
    report_list = (
        ('0','Price Zero'),
        ('1','Not Found'),
        ('2','other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_tracked = models.BooleanField('Tracked', default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Tracking'
        verbose_name_plural = 'Trackings'
        
    def __str__(self):
        return str(self.user) + ' ' + str(self.product)