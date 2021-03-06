# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 02:22
from __future__ import unicode_literals

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text=b'Um nome curto que sera usado para identifica-lo de forma \xc3\xbanica na plataforma', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile(b'^[\\w.@+-]+$'), b'Informe um nome de usu\xc3\xa1rio v\xc3\xa1lidoEste valor deve conter apenas letras, n\xc3\xbamerose os caracteres: @/./+/-/_.', b'invalid')], verbose_name=b'Apelido / Usuario')),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name=b'E-mail')),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'Equipe')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Ativo')),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name=b'Data de Entrada')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
