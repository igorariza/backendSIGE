# Generated by Django 2.1.1 on 2020-05-02 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='managerGroup',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.TeacherUser'),
        ),
    ]
