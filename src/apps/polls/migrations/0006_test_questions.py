# Generated by Django 3.2.6 on 2021-08-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_test_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(to='polls.Question'),
        ),
    ]