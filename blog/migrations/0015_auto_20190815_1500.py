# Generated by Django 2.2.4 on 2019-08-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_merge_20190814_2029'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Django', 'Django'), ('Python', 'Python'), ('C++', 'C++'), ('Graphics', 'Graphics'), ('Text Editor', 'TextEditor'), ('Spreadsheet', 'Spreadsheet'), ('DataBase', 'DataBase'), ('Web Design', 'WebDesign')], max_length=100),
        ),
    ]
