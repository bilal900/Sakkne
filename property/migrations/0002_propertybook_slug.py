# Generated by Django 4.1.6 on 2023-02-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertybook',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
