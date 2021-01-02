from django.db import models
from app.models.users import User
from app.models.retailers import Retailer

class RetailerRaiting(models.Model):
    raiting_list = (
        ('1', 'Very Poor'),
        ('2', 'Poor'),
        ('3', 'Average'),
        ('4', 'Good'),
        ('5', 'Excellent'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    raiting = models.CharField('Raiting', max_length=1, choices=raiting_list)
    comment = models.TextField('Comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Retailer Raiting'
        verbose_name_plural = 'Retailer Raitings'
        
    def __str__(self):
        return str(self.user) + ' ' + str(self.raiting) + ' ' + str(self.product)