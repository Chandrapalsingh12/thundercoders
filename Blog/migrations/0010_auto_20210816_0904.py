# Generated by Django 3.1.7 on 2021-08-16 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_auto_20210814_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo2',
        ),
    ]
