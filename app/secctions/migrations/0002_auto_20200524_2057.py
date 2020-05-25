# Generated by Django 2.1.1 on 2020-05-24 20:57

from django.db import migrations, models
import django.db.models.deletion
import secctions.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('secctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('codeComment', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('dateComment', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResponseSecction',
            fields=[
                ('codeResponse', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.FileField(blank=True, upload_to=secctions.models.get_upload_path)),
                ('messageResponse', models.CharField(max_length=500)),
                ('dateResponse', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='hyperlynks',
            name='secctionHyperlink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lynks', to='secctions.Secction'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource',
            field=models.FileField(blank=True, upload_to=secctions.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='resource',
            name='secctionResource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resources', to='secctions.Secction'),
        ),
        migrations.AlterField(
            model_name='secction',
            name='workspaceSecction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='secctions', to='workspace.WorkSpace'),
        ),
        migrations.AddField(
            model_name='responsesecction',
            name='secctionResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='response', to='secctions.Secction'),
        ),
        migrations.AddField(
            model_name='responsesecction',
            name='studentResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responses', to='users.StudentUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='responseToComment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='secctions.ResponseSecction'),
        ),
        migrations.AddField(
            model_name='comment',
            name='teacherComment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.TeacherUser'),
        ),
    ]
