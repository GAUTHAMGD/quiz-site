# Generated by Django 4.1.13 on 2023-11-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='num_questions',
            field=models.IntegerField(default=0),
        ),
    ]
