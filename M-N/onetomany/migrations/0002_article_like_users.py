# Generated by Django 2.2.5 on 2019-10-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onetomany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(related_name='like_articles', to='onetomany.User'),
        ),
    ]