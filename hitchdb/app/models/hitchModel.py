from django.db import models
from app.models.categories import Category
from app.models.subCategories import SubCategory

class HitchModel(models.Model):
    model = models.CharField('Hitch Model', max_length=50, primary_key=True)
    name = models.CharField('Name', max_length=250)
    segment = models.CharField('Segment', max_length=100)
    image = models.TextField('URL Image')
    # image = models.ImageField('Image', upload_to=None, blank=True, null=True)
    brand = models.CharField('Brand', max_length=250)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'HitchModel'
        verbose_name_plural = 'Hitch Models'
    
    def __str__(self):
        return str(self.model) + ' - ' + str(self.brand)