# Generated by Django 4.2 on 2023-05-25 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_remove_cartproduct_cart_remove_cartproduct_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.product'),
        ),
    ]