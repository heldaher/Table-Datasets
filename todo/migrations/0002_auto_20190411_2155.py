# Generated by Django 2.1.7 on 2019-04-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='downloaded',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='profile_pic',
            field=models.ImageField(default='http://s3.amazonaws.com/37assets/svn/765-default-avatar.png', upload_to='profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='saved',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.TextField(default=''),
        ),
    ]
