# Generated by Django 3.2.6 on 2021-08-14 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210814_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='max_points',
        ),
    ]
