# Generated by Django 2.1.1 on 2020-05-25 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secctions', '0003_auto_20200525_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsesecction',
            name='messageResponse',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='secction',
            name='descriptionSecction',
            field=models.CharField(max_length=5000),
        ),
    ]
