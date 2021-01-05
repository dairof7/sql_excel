from django.db import models
from app.models.users import User
from app.models.product import Product

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_favorite = models.BooleanField('Favorite', default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        
    def __str__(self):
        return str(self.user) + ' ' + str(self.product)
