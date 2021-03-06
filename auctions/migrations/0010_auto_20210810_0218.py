# Generated by Django 3.2.6 on 2021-08-10 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20210810_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.listing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=0, help_text='200 characters max.', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listing',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auctions.user'),
            preserve_default=False,
        ),
    ]
