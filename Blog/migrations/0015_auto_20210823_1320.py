# Generated by Django 3.1.7 on 2021-08-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_auto_20210823_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_thumbnail',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
