# Generated by Django 2.2.20 on 2021-05-17 12:49

from django.db import migrations


def fill_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20210517_1936'),
    ]

    operations = [
        migrations.RunPython(fill_new_building_field),
    ]
