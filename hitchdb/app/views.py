from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView
from .serializers import ProductSerializer, CategorySerializer
from .models.product import Product
from .models.categories import Category
from django.core.cache import cache
# Create your views here.
from django.conf import settings
# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# CACHE_TTL = getattr(settings, 'CACHE_TTL', 50)

class ProductsListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        
        kword = self.kwargs['kword']
        if cache.get(str(kword)):
            print("request attended by Redis")
            data = cache.get(str(kword))
        else:
            data = Product.objects.filter(id=kword)
            cache.set(str(kword), data)
            print("request attended by DB")

        return data

    # queryset = Product.objects.all()


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        if cache.get('cat_list'):
            print("request attended by Redis")
            data = cache.get('cat_list')
        else:
            data = Category.objects.all()
            cache.set('cat_list', data, )
            print("request attended by DB")
        return data
