# Generated by Django 3.2.6 on 2021-08-14 23:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_watchlist_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Bid Date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Comment Date'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]