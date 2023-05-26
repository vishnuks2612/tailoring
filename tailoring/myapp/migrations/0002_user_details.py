# Generated by Django 3.2.15 on 2022-10-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=200)),
                ('addr', models.CharField(max_length=500)),
                ('pin', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('email', models.CharField(max_length=25)),
            ],
        ),
    ]
