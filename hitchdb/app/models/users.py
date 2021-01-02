from django.db import models
from django.contrib.auth.models import User
from app.models.countries import Country


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(, max_length=50)
    # email = models.EmailField(, max_length=254)
    fcm_token = models.CharField('Token', max_length=50)
    status = models.IntegerField(default=1)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # is_active = models.BinaryField(default=True)
    # created = models.DateField(auto_now_add=True)
    # updated = models.DateField(auto_now=True)
    # image?
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)