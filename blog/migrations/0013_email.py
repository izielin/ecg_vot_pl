# Generated by Django 2.2.4 on 2019-08-14 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_auto_20190813_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(default='ecg.vot@gmail.com', max_length=100)),
                ('receivers', models.TextField(default="['test@test.pl']", max_length=500)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('posted', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(blank=True, null=True)),
                ('subject', models.TextField(default='Subject', max_length=100)),
                ('message', models.TextField(default='message', max_length=1000)),
                ('author', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usernames', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
