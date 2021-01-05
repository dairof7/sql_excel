from django.db import models

class Category(models.Model):
    spanish = models.CharField('Spanish', max_length=150)
    english = models.CharField('English', max_length=150)
    portuguese = models.CharField('Portuguese', max_length=150)
    # image = models.CharField('Image URL', max_length=255)
    image = models.ImageField('Image', upload_to=None, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return str(self.english)

