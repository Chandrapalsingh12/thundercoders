# Generated by Django 3.1.7 on 2021-08-30 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0019_auto_20210830_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Blog.category'),
        ),
    ]
