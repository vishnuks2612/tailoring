# Generated by Django 3.2.15 on 2022-11-14 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_product_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='quant',
        ),
    ]
