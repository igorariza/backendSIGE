# Generated by Django 3.0.3 on 2020-04-11 22:09

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('codeUser', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('documentIdUser', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Numero incorrecto', regex='^\\+?1?\\d{7,10}$')])),
                ('typeIdeUser', models.CharField(max_length=100)),
                ('firstNameUser', models.CharField(max_length=100)),
                ('lastNameUser', models.CharField(max_length=100)),
                ('emailUser', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('phoneUser', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Numero incorrecto', regex='^\\+?1?\\d{7,10}$')])),
                ('addressUser', models.CharField(max_length=50)),
                ('passwordUser', models.CharField(default=[models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Numero incorrecto', regex='^\\+?1?\\d{7,10}$')])], max_length=20)),
                ('dateOfBirthUser', models.DateField(default=datetime.date.today)),
                ('dateLastAccessUser', models.DateField(default=datetime.date.today)),
                ('genderUser', models.CharField(max_length=20)),
                ('rhUser', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('codeHeadquartersUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.Headquarters')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherUser',
            fields=[
                ('codeTeacher', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degreesTeacher', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('codeStudent', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('codeStaff', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupationStaff', models.PositiveSmallIntegerField(choices=[(1, 'principal'), (2, 'subprincial'), (3, 'payer'), (4, 'assistant'), (5, 'assistantSIMAT')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RelativeUser',
            fields=[
                ('codeRelative', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeRelative', models.PositiveSmallIntegerField(choices=[(1, 'parent'), (2, 'attending')])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.StudentUser')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
