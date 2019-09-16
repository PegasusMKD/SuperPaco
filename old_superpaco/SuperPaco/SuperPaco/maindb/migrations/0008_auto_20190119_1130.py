# Generated by Django 2.1.5 on 2019-01-19 11:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0007_auto_20181216_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='id',
            name='neutral_choices',
        ),
        migrations.AddField(
            model_name='id',
            name='choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(blank=True), blank=True, null=True, size=None), blank=True, null=True, size=None),
        ),
    ]