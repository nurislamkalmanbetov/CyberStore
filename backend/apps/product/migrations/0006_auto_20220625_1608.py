# Generated by Django 3.2.9 on 2022-06-25 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
