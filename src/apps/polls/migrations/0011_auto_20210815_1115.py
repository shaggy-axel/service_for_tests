# Generated by Django 3.2.6 on 2021-08-15 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0010_remove_test_max_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='max_points',
        ),
        migrations.RemoveField(
            model_name='result',
            name='points_earned',
        ),
        migrations.RemoveField(
            model_name='result',
            name='quantity_of_question',
        ),
        migrations.AddField(
            model_name='result',
            name='test',
            field=models.ManyToManyField(to='polls.Test'),
        ),
        migrations.AlterField(
            model_name='result',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
