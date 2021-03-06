# Generated by Django 3.2.6 on 2021-08-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210813_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='RightChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
            options={
                'verbose_name': 'Правильный Ответ',
                'verbose_name_plural': 'Правильные Ответы',
                'db_table': 'right_choices',
            },
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Вариант Ответа', 'verbose_name_plural': 'Варианты Ответов'},
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.ManyToManyField(related_name='correct_answer', to='polls.RightChoice'),
        ),
    ]
