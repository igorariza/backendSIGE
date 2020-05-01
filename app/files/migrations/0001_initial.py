# Generated by Django 2.1.1 on 2020-05-01 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('codeEvidence', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameEvidence', models.CharField(max_length=100)),
                ('descriptionEvidence', models.CharField(max_length=255)),
                ('typeEvidence', models.PositiveSmallIntegerField(choices=[(1, 'Clase Virtual'), (2, 'Material')])),
            ],
            options={
                'ordering': ['codeEvidence'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('codeFile', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadOnFile', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, upload_to='evidences/')),
            ],
        ),
        migrations.AddField(
            model_name='evidence',
            name='file',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='files.File'),
        ),
    ]
