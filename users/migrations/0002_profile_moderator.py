# Generated by Django 2.2.2 on 2019-06-29 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='moderator',
            field=models.BooleanField(default=True),
        ),
    ]
