# Generated by Django 2.1.1 on 2020-07-30 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secctions', '0014_auto_20200730_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]
