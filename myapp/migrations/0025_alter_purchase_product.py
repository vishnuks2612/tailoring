# Generated by Django 4.2 on 2023-05-25 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_purchase_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product'),
        ),
    ]
