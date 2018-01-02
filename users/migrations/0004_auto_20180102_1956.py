# Generated by Django 2.0 on 2018-01-02 19:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_account_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.TextField(default=None, null=True)),
                ('uploaded', models.DateTimeField(default=datetime.datetime.now, verbose_name='uploaded on')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='about',
            field=models.TextField(default=None, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='website',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldsrelatedonetoonefield', unique=True),
        ),
        migrations.AddField(
            model_name='account',
            name='picture',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='users.Picture'),
        ),
    ]
