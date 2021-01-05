from django.contrib import admin
from django.urls import path
from . import views

app_name = 'products_app'

urlpatterns = [
    path('list/<kword>/', views.ProductsListAPIView.as_view(), name='products_list'),
    path('cat_list/', views.CategoryListAPIView.as_view(), name='category_list'),
]