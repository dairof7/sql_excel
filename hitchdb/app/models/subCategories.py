from django.db import models
from app.models.categories import Category


class SubCategory(models.Model):
    spanish = models.CharField('Spanish', max_length=50)
    english = models.CharField('English', max_length=50)
    portuguese = models.CharField('Portuguese', max_length=50)
    # image = models.CharField('Image URL', max_length=255)
    image = models.ImageField('Image', upload_to=None, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'
    
    def __str__(self):
        return str(self.english)