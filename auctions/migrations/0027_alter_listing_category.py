# Generated by Django 3.2.6 on 2021-08-17 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('fashion', 'Fashion'), ('toys', 'Toys'), ('electronics', 'Electronics'), ('home', 'Home'), ('sports', 'Sports'), ('other', 'Other')], max_length=11, verbose_name='Category (optional)'),
        ),
    ]
