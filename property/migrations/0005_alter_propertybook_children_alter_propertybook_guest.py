# Generated by Django 4.1.6 on 2023-03-04 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_rename_sllug_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='children',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='guest',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
