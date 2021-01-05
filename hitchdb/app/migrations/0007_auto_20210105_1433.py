# Generated by Django 3.1.2 on 2021-01-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201230_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='english',
            field=models.CharField(max_length=150, verbose_name='English'),
        ),
        migrations.AlterField(
            model_name='category',
            name='portuguese',
            field=models.CharField(max_length=150, verbose_name='Portuguese'),
        ),
        migrations.AlterField(
            model_name='category',
            name='spanish',
            field=models.CharField(max_length=150, verbose_name='Spanish'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(max_length=50, unique=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='historyprice',
            name='price',
            field=models.CharField(default='0', max_length=150, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='current_price',
            field=models.CharField(default='0', max_length=50, verbose_name='Current Price'),
        ),
        migrations.AlterField(
            model_name='productraiting',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='report',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='image',
            field=models.TextField(blank=True, null=True, verbose_name='URL Image'),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='retailer',
            field=models.CharField(max_length=150, unique=True, verbose_name='Retailer'),
        ),
        migrations.AlterField(
            model_name='retailerraiting',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
    ]