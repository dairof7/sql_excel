from django.db import models
from app.models.users import User
from app.models.product import Product

class Report(models.Model):
    report_list = (
        ('0','Price Zero'),
        ('1','Not Found'),
        ('2','other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    status = models.IntegerField(default=1)
    report_type = models.CharField('Report Type', max_length=1, choices=report_list)
    comment = models.TextField('Comment', blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
        
    def __str__(self):
        
        return str(self.user) + ' ' + str(self.report_list[int(self.report_type)])