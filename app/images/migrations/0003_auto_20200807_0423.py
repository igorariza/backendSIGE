# Generated by Django 2.1.1 on 2020-08-07 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20200807_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageresponse',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='secctions.Responses'),
        ),
    ]
