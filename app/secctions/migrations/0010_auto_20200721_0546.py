# Generated by Django 2.1.1 on 2020-07-21 05:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('secctions', '0009_secction_date_close'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secction',
            name='date_close',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
