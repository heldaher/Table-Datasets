# Generated by Django 2.1.7 on 2019-04-11 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190411_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
