# Generated by Django 2.2.3 on 2019-08-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190805_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='b1.jpg', upload_to='post_pic'),
        ),
    ]
