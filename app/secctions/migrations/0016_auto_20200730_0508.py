# Generated by Django 2.1.1 on 2020-07-30 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secctions', '0015_auto_20200730_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='response_secction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='homework', to='secctions.Responses'),
        ),
    ]
