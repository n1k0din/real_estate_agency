# Generated by Django 2.2.20 on 2021-05-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(verbose_name='Новостройка?'),
        ),
    ]
