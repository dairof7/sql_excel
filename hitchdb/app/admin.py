from django.contrib import admin
from .models import historyPrice, product, retailers, users, userReports
from .models import categories, hitchModel, subCategories, countries
from .models import productRaiting, favorites, tracking, retailerRaiting

class HitchModelAdmin(admin.ModelAdmin):

    list_display=(
        'name',
        'model',
        'segment',
        # 'image',
        'brand',
        'category',
        'sub_category',
    )
    search_fields = ('name','model')
    list_filter = ('brand',)
    
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=('id','english', 'category')

class ProductAdmin(admin.ModelAdmin):
    list_display=(
        'hitch_model',
        'current_price',
        'enable',
        'issue_report',
        'country',
        'retailer',
    )
    search_fields = ('hitch_model',)
    list_filter = ('country', 'retailer', 'enable', 'issue_report')

admin.site.register(hitchModel.HitchModel, HitchModelAdmin)
admin.site.register(categories.Category)
admin.site.register(subCategories.SubCategory, SubCategoryAdmin)

admin.site.register(retailers.Retailer)
admin.site.register(product.Product, ProductAdmin)
admin.site.register(countries.Country)
admin.site.register(historyPrice.HistoryPrice)
admin.site.register(users.User)
admin.site.register(userReports.Report)
admin.site.register(productRaiting.ProductRaiting)
admin.site.register(favorites.Favorite)
admin.site.register(tracking.Tracking)
admin.site.register(retailerRaiting.RetailerRaiting)




