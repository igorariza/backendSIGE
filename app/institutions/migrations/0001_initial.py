# Generated by Django 2.1.1 on 2020-05-02 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalInstitution',
            fields=[
                ('nameIE', models.CharField(max_length=100, unique=True)),
                ('nitIE', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Headquarters',
            fields=[
                ('codeHeadquarters', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daneHeadquarters', models.CharField(max_length=100)),
                ('nameHeadquarters', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('ieHeadquarters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.EducationalInstitution')),
            ],
        ),
    ]
