# Generated by Django 2.0 on 2017-12-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20171214_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='filled',
            field=models.BooleanField(default=False),
        ),
    ]