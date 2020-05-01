# Generated by Django 2.1.1 on 2020-05-01 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HyperLynks',
            fields=[
                ('codeHyperLink', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('codeResouce', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.FileField(blank=True, upload_to='resources/')),
            ],
        ),
        migrations.CreateModel(
            name='Secction',
            fields=[
                ('codeSecction', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSecction', models.CharField(max_length=100)),
                ('descriptionSecction', models.CharField(max_length=255)),
                ('uploadOnSecction', models.DateTimeField(auto_now_add=True)),
                ('workspaceSecction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secctions', to='workspace.WorkSpace')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='secctionResource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='secctions.Secction'),
        ),
        migrations.AddField(
            model_name='hyperlynks',
            name='secctionHyperlink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lynks', to='secctions.Secction'),
        ),
    ]
