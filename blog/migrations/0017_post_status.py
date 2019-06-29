# Generated by Django 2.2.2 on 2019-06-29 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190629_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Work-In-Progress', 'Work-In-Progress'), ('Not-Approved-Yet', 'Not-Approved-Yet')], default='Not-Approved-Yet', max_length=100),
        ),
    ]
