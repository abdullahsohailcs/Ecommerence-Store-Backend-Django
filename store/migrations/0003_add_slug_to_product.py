# Generated by Django 4.2.2 on 2023-07-02 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_to_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='-'),
            preserve_default=False,
        ),
    ]
