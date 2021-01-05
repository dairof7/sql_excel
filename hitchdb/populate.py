import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hitchdb.settings")
django.setup()

from faker import Faker
from app.models.categories import Category
from app.models.subCategories import SubCategory
from app.models.hitchModel import HitchModel
from app.models.countries import Country
from app.models.retailers import Retailer
from app.models.historyPrice import HistoryPrice
from app.models.retailerRaiting import RetailerRaiting
from app.models.tracking import Tracking
from app.models.favorites import Favorite
from app.models.productRaiting import ProductRaiting
from app.models.userReports import Report
from app.models.product import Product
from django.utils import timezone


# categories = ['AUDIO', 'COMPUTING', 'TELEPHONY', 'VIDEOGAMES']
sub_categories = {
    'COMPUTING': ['COMPUTERS', 'ACCESORIES'],
    'AUDIO': ['SOUNDBARS', 'MINISTEREOS', 'MICROSTEREOS', 'SPEAKERS'],
    'TELEPHONY': ['CELLPHONES'],
    'VIDEOGAMES': ['CONSOLES', 'ACCESORIES']
} 
def create_category():
    fake = Faker()
    for x in sub_categories.keys():
        name = x
        # print(name)
        Category.objects.create(spanish=name,
        english=name,
        portuguese=name,
        created = timezone.now(),
        updated = timezone.now(),
        )

def create_subcategory():
    fake = Faker()
    for key, val in sub_categories.items():
        for sub_cat in val:
            name = sub_cat
            # print(name)
            SubCategory.objects.create(
            spanish=name,
            english=name,
            portuguese=name,
            category=Category.objects.get(english=key),
            # print(category)
            created = timezone.now(),
            updated = timezone.now(),
            )

def create_hitchModel(N):
    fake = Faker()
    for n in range(N):
        # print(list(sub_categories.keys()))
        cat = random.choice(list(sub_categories.keys()))
        sub_cat = random.choice(list(sub_categories[cat]))

        fk_category = Category.objects.get(english=cat)
        # print(hitch_model)
        HitchModel.objects.create(
        model=fake.unique.bothify('########-????????'),
        name=fake.bothify('??????????'),
        segment=fake.color(),
        image=fake.image_url(),
        brand=fake.company_suffix(),
        created = timezone.now(),
        updated = timezone.now(),
        category=fk_category,
        sub_category=SubCategory.objects.get(english=sub_cat,category=fk_category),
        # print(category)
        # print(sub_category)

        )

def create_countries(N):
    fake = Faker()
    for n in range(N):
        Country.objects.create(
        country=fake.unique.country(),
        created = timezone.now(),
        updated = timezone.now(),
        )

def create_retailer(N):
    fake = Faker()
    all_countries = Country.objects.all()
    for n in range(N):
        Retailer.objects.create(
        retailer=fake.bs(),
        image=fake.image_url(),
        country=random.choice(all_countries),
        created = timezone.now(),
        updated = timezone.now(),
        )

def create_product(N):
    fake = Faker()
    all_hitchModel = HitchModel.objects.all()
    all_retailer = Retailer.objects.all()
    all_countries = Country.objects.all()
    for n in range(N):
        Product.objects.create(
        url=fake.url(),
        current_price=fake.numerify('#####'),
        enable=fake.pybool(),
        issue_report=fake.pybool(),
        country=random.choice(all_countries),
        retailer=random.choice(all_retailer),
        hitch_model=random.choice(all_hitchModel),
        created = timezone.now(),
        updated = timezone.now(),
        # print('{}-{}-{}'.format(country,retailer,hitch_model))
        )

def create_history(N):
    fake = Faker()
    all_products = Product.objects.all()
    for n in range(N):
        HistoryPrice.objects.create(
            price=random.randint(0,5000),
            product=random.choice(all_products),
            created = timezone.now(),
            updated = timezone.now(),
        )

create_category()
create_subcategory()
create_hitchModel(9)
create_countries(17)
create_retailer(9)
create_product(9)
create_history(20)
print('Terminado!!!!!!!!!!!')