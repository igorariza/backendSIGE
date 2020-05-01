# Generated by Django 2.1.1 on 2020-05-01 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('nameGroup', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('headquarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.Headquarters')),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('codeJourney', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameJourney', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='journeyGroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='groups.Journey'),
        ),
    ]
