# Generated by Django 2.1.2 on 2019-01-20 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0002_id_time_stamps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='id',
            name='something',
        ),
        migrations.RemoveField(
            model_name='id',
            name='time_stamps',
        ),
    ]