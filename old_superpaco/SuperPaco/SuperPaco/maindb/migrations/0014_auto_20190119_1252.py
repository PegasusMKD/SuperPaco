# Generated by Django 2.1.5 on 2019-01-19 12:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0013_auto_20190119_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id',
            name='choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(blank=True), blank=True, default=list, null=True, size=None), blank=True, default=list, null=True, size=None),
        ),
    ]
