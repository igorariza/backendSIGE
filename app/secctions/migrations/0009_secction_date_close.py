# Generated by Django 2.1.1 on 2020-07-21 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secctions', '0008_comment_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='secction',
            name='date_close',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 21, 5, 45, 16, 828603)),
        ),
    ]
