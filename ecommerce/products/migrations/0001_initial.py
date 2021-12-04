# Generated by Django 3.2.9 on 2021-12-04 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=255, verbose_name='CategoryName')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('sku', models.CharField(max_length=100, unique=True, verbose_name='SKU')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(max_length=2000, verbose_name='Description')),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('white', 'White'), ('yellow', 'Yellow')], max_length=20, verbose_name='Color')),
                ('size', models.CharField(max_length=30, verbose_name='Size')),
                ('categories', models.ManyToManyField(to='products.Category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'stock',
                'verbose_name_plural': 'stocks',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'price',
                'verbose_name_plural': 'prices',
            },
        ),
    ]
