# Generated by Django 2.2.28 on 2025-02-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0010_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
