# Generated by Django 3.2.15 on 2022-10-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='', upload_to='./myapp/images'),
        ),
    ]
