# Generated by Django 3.2.6 on 2021-08-10 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210810_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='starting_price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
