# Generated by Django 2.1.1 on 2020-07-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secctions', '0010_auto_20200721_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='secction',
            name='image_found',
            field=models.CharField(default='https://res.cloudinary.com/duyflkcyn/image/upload/v1595312014/SIGE/ActivitiesPhothos/3_talrgu.jpg', max_length=5000, null=True),
        ),
    ]
