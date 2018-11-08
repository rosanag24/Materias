# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 07:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0010_auto_20181107_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='dirección de correo')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates whether the user can log into this site.', verbose_name='superuser status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', posts.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('codigoMateria', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nombreMateria', models.CharField(max_length=60)),
                ('unidadesCredito', models.IntegerField()),
                ('area', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('codigoDepartamento', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombreDepartamento', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('cedulaIdentidad', models.IntegerField(primary_key=True, serialize=False)),
                ('primerNombre', models.CharField(max_length=15)),
                ('segundoNombre', models.CharField(blank=True, default='', max_length=15)),
                ('primerApellido', models.CharField(max_length=15)),
                ('segundoApellido', models.CharField(max_length=15)),
                ('fechaRegistro', models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')),
                ('codigoDepartamento1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('codigoPrograma', models.IntegerField(primary_key=True, serialize=False)),
                ('nombrePrograma', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('codigoRol', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreRol', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Rol'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='departamento',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='posts.Departamento'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='programaPertenece',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Programa'),
        ),
    ]
